# 🔐 Advanced Password Strength Checker (CLI)

A Python command-line tool that evaluates password strength with advanced heuristics.  
It goes beyond simple length checks by analyzing dictionary words, leetspeak, sequences, repeated characters, context identifiers, known breaches, and more.  
Also includes password and passphrase generators.

---

## ✨ Features

- **Dictionary check**  
  Detects dictionary substrings (direct and leetspeak) using a 2.3M-word list.  [dictionary that use](https://huggingface.co/datasets/Maximax67/English-Valid-Words)

- **Pattern detection**  
  Finds repeated characters, sequential numbers/letters, keyboard patterns, and year/date strings.  

- **Context awareness**  
  Detects if the password contains usernames, emails, or site names you add via CLI.  

- **Breach check**  
  Integrates with Have I Been Pwned (HIBP) API, with optional offline suffix file.  

- **Entropy & score**  
  Estimates entropy, applies penalties, and outputs a normalized score (0–100).  

- **Crack-time estimate**  
  Approximates time to crack in three scenarios:  
  - Online throttled (100 guesses/sec)  
  - Offline moderate (10⁸ guesses/sec)  
  - Offline fast (10¹⁰ guesses/sec)  

- **Password generator**  
  Generates strong random passwords with letters, digits, and symbols.  

- **Passphrase generator**  
  Generates secure multi-word passphrases that are easier to remember but very strong.  

- **Colorful CLI**  
  Easy-to-read results using `colorama`.  

