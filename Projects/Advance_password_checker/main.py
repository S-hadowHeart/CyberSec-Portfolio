import math, hashlib, os, sys, random, re, string
from colorama import Fore, Style, init
init(autoreset=True)

try:
    import requests
except:
    requests = None

WORDLIST_PATH = "words.txt"
LOCAL_PWNED_SUFFIX_FILE = "pwned_suffixes.txt"
HIBP_RANGE_URL = "https://api.pwnedpasswords.com/range/{}"
LEET_MAP = str.maketrans({'@':'a','4':'a','0':'o','1':'l','3':'e','5':'s','$':'s','7':'t','+':'t','8':'b','2':'z'})
KEYBOARD_SEQS = ["qwertyuiop","asdfghjkl","zxcvbnm","1234567890","poiuytrewq","lkjhgfdsa","mnbvcxz"]
COMMON_PASSWORDS_SMALL = {"password","123456","123456789","qwerty","abc123","football","iloveyou","admin","welcome","monkey","letmein","dragon","baseball","master"}

def load_wordset(path=WORDLIST_PATH):
    s = set()
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            w = line.strip().lower()
            if w: s.add(w)
    return s

def sha1_hex_upper(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest().upper()

def check_pwned_hibp(pw, timeout=5.0):
    if requests is None: return -1
    h = sha1_hex_upper(pw)
    prefix, suffix = h[:5], h[5:]
    try:
        r = requests.get(HIBP_RANGE_URL.format(prefix), headers={"User-Agent":"PasswordChecker/1.0"}, timeout=timeout)
    except:
        return -1
    if r.status_code != 200: return -1
    for line in r.text.splitlines():
        if not line: continue
        parts = line.split(":")
        if len(parts) != 2: continue
        suf, cnt = parts[0].strip(), parts[1].strip()
        if suf.upper() == suffix:
            try:
                return int(cnt)
            except:
                return 1
    return 0

def load_local_pwned(path=LOCAL_PWNED_SUFFIX_FILE):
    d = {}
    if not os.path.exists(path): return d
    with open(path,"r",encoding="utf-8",errors="ignore") as f:
        for line in f:
            if ":" not in line: continue
            suf,cnt=line.strip().split(":",1)
            try:
                d[suf.strip().upper()] = int(cnt.strip())
            except:
                d[suf.strip().upper()] = 1
    return d

_LOCAL_PWNED = load_local_pwned()

def check_pwned_offline(pw):
    if not _LOCAL_PWNED: return 0
    return _LOCAL_PWNED.get(sha1_hex_upper(pw)[5:],0)

def leet_normalize(s):
    return s.translate(LEET_MAP)

def all_substrings(s, min_len=3):
    s = s.lower()
    n = len(s)
    for i in range(n):
        for j in range(i+min_len, n+1):
            yield s[i:j]

def dict_matches(pw, wordset, min_len=3):
    found = set()
    subs = set(all_substrings(pw, min_len=min_len))
    for sub in subs:
        if sub in wordset:
            found.add(sub)
        else:
            ln = leet_normalize(sub)
            if ln in wordset:
                found.add(sub)
    return sorted(found)

def detect_repeated_runs(pw):
    runs = []
    if not pw: return runs
    cur = pw[0]
    cnt = 1
    for ch in pw[1:]:
        if ch == cur:
            cnt += 1
        else:
            if cnt >= 3:
                runs.append((cur, cnt))
            cur = ch
            cnt = 1
    if cnt >= 3:
        runs.append((cur, cnt))
    return runs

def detect_sequences(pw):
    found = []
    lowered = pw.lower()
    n = len(lowered)
    for L in (4,3):
        for i in range(n - L + 1):
            chunk = lowered[i:i+L]
            if chunk.isalpha() and all(ord(chunk[j+1]) - ord(chunk[j]) == 1 for j in range(len(chunk)-1)):
                found.append(("alpha_seq", chunk))
            if chunk.isdigit() and all(int(chunk[j+1]) - int(chunk[j]) == 1 for j in range(len(chunk)-1)):
                found.append(("num_seq", chunk))
    for seq in KEYBOARD_SEQS:
        for L in range(3, min(7, len(seq))+1):
            for i in range(len(seq)-L+1):
                sub = seq[i:i+L]
                if sub in lowered or sub[::-1] in lowered:
                    found.append(("keyboard", sub))
    return found

def detect_years(pw):
    return re.findall(r"(19\d{2}|20\d{2})", pw)

def is_email_like(pw):
    return "@" in pw and re.search(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", pw) is not None

def entropy_bits(pw):
    length = len(pw)
    classes = 0
    if any(c.islower() for c in pw): classes += 26
    if any(c.isupper() for c in pw): classes += 26
    if any(c.isdigit() for c in pw): classes += 10
    if any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/|\\`~" for c in pw): classes += 32
    if classes == 0: return 0.0
    return round(length * math.log2(classes), 2)

def bits_to_score(bits):
    if bits <= 0: return 0
    if bits < 40: return int((bits / 40) * 30)
    if bits < 60: return 30 + int(((bits - 40) / 20) * 30)
    if bits < 80: return 60 + int(((bits - 60) / 20) * 25)
    if bits < 100: return 85 + int(((bits - 80) / 20) * 15)
    return 100

def crack_times_seconds(effective_bits):
    guesses = 2 ** effective_bits if effective_bits > 0 else 1
    scenarios = {"online_throttled_100_s":100,"offline_moderate_1e8_s":1e8,"offline_fast_1e10_s":1e10}
    return {k: guesses / v for k,v in scenarios.items()}

def human_time(seconds):
    if seconds < 1e-6: return "instant"
    intervals = (('years',31536000),('days',86400),('hours',3600),('minutes',60),('seconds',1))
    parts = []
    for name,count in intervals:
        v = int(seconds // count)
        if v:
            parts.append(f"{v} {name}")
            seconds -= v * count
    return ", ".join(parts[:2]) if parts else "less than a second"

def generate_password(length=16, use_symbols=True):
    chars = string.ascii_letters + string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+[]{};:'\",.<>?/|\\`~"
    return ''.join(random.SystemRandom().choice(chars) for _ in range(length))

def generate_passphrase(wordset, num_words=4, separator='-', add_number=True, add_symbol=True):
    words = random.sample(list(wordset), num_words)
    phrase = separator.join(words)
    if add_number:
        phrase += str(random.randint(0, 99))
    if add_symbol:
        phrase += random.choice("!@#$%^&*")
    return phrase

def analyze_password(pw, wordset, context_identifiers=None, use_hibp=True):
    if context_identifiers is None: context_identifiers = []
    res = {}
    res['password'] = pw
    res['length'] = len(pw)
    raw_bits = entropy_bits(pw)
    penalties = 0.0
    issues = []
    suggestions = []
    dicts = dict_matches(pw, wordset, min_len=3)
    if dicts:
        issues.append("Contains dictionary substring(s): " + ", ".join(dicts[:6]) + ("..." if len(dicts)>6 else ""))
        suggestions.append("Avoid dictionary words or substrings.")
        penalties += sum(len(x) * 2 for x in dicts)
    low = pw.lower()
    if low in COMMON_PASSWORDS_SMALL or any(c in low for c in COMMON_PASSWORDS_SMALL):
        issues.append("Matches or contains a common password.")
        suggestions.append("Do not use common passwords or slight variants.")
        penalties += 40
    yrs = detect_years(pw)
    if yrs:
        issues.append("Contains year/date-like pattern: " + ", ".join(yrs))
        suggestions.append("Avoid including years or birthdays.")
        penalties += 15
    repeats = detect_repeated_runs(pw)
    if repeats:
        for ch,cnt in repeats:
            issues.append(f"Repeated character '{ch}' x {cnt}")
            suggestions.append("Avoid long repeated runs of the same character.")
            penalties += (cnt - 2) * 3
    seqs = detect_sequences(pw)
    if seqs:
        seqstr = ", ".join(f"{t}:{s}" for t,s in seqs[:6])
        issues.append("Detected simple sequences/patterns: " + seqstr)
        suggestions.append("Avoid simple sequences and keyboard patterns.")
        penalties += sum(len(s) * 2 for _,s in seqs)
    if is_email_like(pw):
        issues.append("Password looks like an email or contains email-like pattern.")
        suggestions.append("Avoid using emails or email-like strings as passwords.")
        penalties += 20
    for ident in context_identifiers:
        if ident and ident.lower() in low:
            issues.append("Contains context identifier: " + ident)
            suggestions.append("Do not include username, site name, or email parts.")
            penalties += len(ident) * 3
    breach_penalty = 0.0
    breach_count = 0
    if use_hibp:
        cnt = check_pwned_hibp(pw)
        used_offline = False
        if cnt == -1:
            cnt = check_pwned_offline(pw)
            used_offline = True
        if cnt and cnt > 0:
            breach_count = cnt
            issues.append(f"Found in public breaches: seen {cnt:,} times")
            suggestions.append("This password has appeared in breaches — change and avoid reuse.")
            breach_penalty = min(80.0, math.log2(max(1,cnt)) + 20)
            penalties += breach_penalty
    effective_bits = max(0.0, raw_bits - penalties)
    res['raw_bits'] = round(raw_bits,2)
    res['penalty_bits'] = round(penalties,2)
    res['effective_bits'] = round(effective_bits,2)
    score = bits_to_score(effective_bits)
    if len(pw) >= 16:
        score = min(100, score + 5)
    res['score'] = score
    if score < 20: label = "Very Weak"
    elif score < 40: label = "Weak"
    elif score < 60: label = "Fair"
    elif score < 80: label = "Strong"
    else: label = "Very Strong"
    res['label'] = label
    res['issues'] = issues if issues else ["No obvious weak patterns found."]
    res['suggestions'] = list(dict.fromkeys(suggestions))
    res['breach_count'] = breach_count
    return res

def display_result(res):
    print(Fore.CYAN + "=== Password Analysis ===" + Style.RESET_ALL)
    print("Password:", Fore.WHITE + ("*" * len(res['password'])) + Style.RESET_ALL)
    print("Strength:", (Fore.RED if res['score']<40 else Fore.YELLOW if res['score']<60 else Fore.GREEN) + f"{res['label']} ({res['score']}/100)" + Style.RESET_ALL)
    print(f"Length: {res['length']}  Raw bits: {res['raw_bits']}  Penalty bits: {res['penalty_bits']}  Effective bits: {res['effective_bits']}")
    if res['breach_count'] > 0:
        print(Fore.RED + f"BREACHED: seen {res['breach_count']:,} times in public leaks!" + Style.RESET_ALL)
    print("Issues:")
    for i in res['issues']:
        print(" -", i)
    print("Suggestions:")
    for s in res['suggestions']:
        print(" -", s)
    times = crack_times_seconds(res['effective_bits'])
    print("Estimated crack times:")
    for k,v in times.items():
        print(f" - {k.replace('_',' ')}: {human_time(v)}")
    print(Fore.CYAN + "="*25 + Style.RESET_ALL)

def main():
    if not os.path.exists(WORDLIST_PATH):
        print(Fore.RED+f"Wordlist {WORDLIST_PATH} not found."+Style.RESET_ALL)
        sys.exit(1)
    wordset = load_wordset()
    print(Fore.CYAN + "Password Checker CLI. Commands: 'quit'/'exit', 'gen', 'passphrase'" + Style.RESET_ALL)
    context_identifiers = []
    while True:
        pw = input(
            Fore.WHITE+"Enter password (or 'q' to quit, 'gen' for password, 'passphrase' for passphrase): "
            +Style.RESET_ALL
        ).strip()
        if not pw: continue
        if pw.lower() in ['q','quit','exit']:
            break
        elif pw.lower() == 'gen':
            print(Fore.CYAN+"Generated strong password: "+Style.RESET_ALL, generate_password())
            continue
        elif pw.lower() == 'passphrase':
            print(Fore.CYAN+"Generated passphrase: "+Style.RESET_ALL, generate_passphrase(wordset))
            continue
        elif pw.lower().startswith("context add "):
            ident = pw[12:].strip()
            if ident: context_identifiers.append(ident)
            print(Fore.YELLOW+"Added context identifier:", ident)
            continue
        res = analyze_password(pw, wordset, context_identifiers=context_identifiers)
        display_result(res)
        print()

if __name__=="__main__":
    main()
