# Approach 
- Understand what an appliaction/feature does
- click every button (sometimes do some fuzzing)
- identify interesting endpoints
- security implications/controls

## Understand the application
- Takes a few hours
- How is a regular user supposed to use the app?
- what can they do? How does it work? What's the point
- More complex the better -harder to learn but also applies to other hackers too
    - Also tends to have complex, easy to break security controls
- if you know the app well you can skip this

## Key Features
- By the end of this process , you should know the key features and how to use them
- You should have all the accounts you need and organisations/permissions
- Ready to use like an actual user
- We should understand what kind of vulnerbilities to look for
    - it's call "litmus tests"

## Find lesser-known Features
- Once you know the app and it's major features you can start to look for lesser-known features
- Dig into hamburger menus
- Look at API routes vs parameters
- Find developer/power user features
- Look at integrations with other apps
  - These are FULL of bugs

### Dig into Obscure use-cases
- Same as before - look at things no other hacker looks at
- while you may not have a large subdomain scope - apps have scope in terms of features
- This might be developers integrations, hacks put together, IFTTT etc..

### Finding Newer Functionality
- Always read blogs and patch notes
- identify new features as soon as they are available and hack that
- Less hackers,less competition
    - but also less oversight and potentially automated deployments
- But also potentially features that haven't been tested
    - We saw this a lot when ChatGot was announced
    - Suddenly a lot of companies implemented AI features
    - First to market but not fully tested

### Automated Fuzzing
- Tools
    - kiterunner for APIs
    - Shodan for CVEs
    - Discord for alerts/callbacks
    - -Nuclei for scanning but everyone is running Nuclei so a waste of time for bug bounty
    - AMASS for subdomains
    - Ffuz for traditional fuzzing

### What is an interesting endpoint?
- looking for signs of vulnerabilities...
- ID = IDOR
- Reflected input = XSS
- Complex processes = Business Logic
- Lots of data = Information exposure

### The Cycle
--> Try Exploit --> Doesn't Work --> Work out why --> Change exploit -->

### Interesting ==> Vulnerable
- Try to perform a test for the bug
   - i'm looking for
       - IDOR = change ID
       - XSS = simple XSS payload
- Did it work ?
    - Write a full exploit to show as a PoC
- Did it fail ?
    - Why did it fail? Eg filtered
    - Restest with a change

### Before Report 
- is there a winder security issue at play ?
    - E.g. 1 IDOR vs Full authoriztion missing from application
- Chains of bugs
    - E.g. User update IDOR , Change password = Account takeover
- Impact impact impact
    - weird functionality or genuine seurity concern? what could an attacker do and WHY

### What Does This Program Care About?
- Foucs my testing on things clients care about
- General top priority issues:
    - Data protection/GDPR
    - Account/organisation takeovers
    - Remote code/Command execution
- Low Priority Issues
    - Social engineering
    - unrealistic attacks

### What Security Controls Are in Place?
- Often gives you an idea of what kind of bugs have been found previously
- As well as bypasses e.g. cloudflare
- Focus on breaking those controls

### Tips
- Understand first then hack
- Don't get intimidated by a scope , break it down into funtions
- if it's an older program don't assume everything is found but also look for lesser known features
- Read the scope page, see what the company wants you to focus on
- Get into hamburger menus and find new scope that no one else knows about

