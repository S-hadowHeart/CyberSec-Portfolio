# Analysing the DOM to Find Reflected XSS

## Introduction
- Explores Reflected Cross-Site Scripting (XSS), a common web vulnerability where user input is echoed by the application without proper sanitization, allowing attackers to inject malicious JavaScript.
- Successful XSS enables actions beyond pop-ups, such as account takeovers, phishing attacks, and cookie theft.

## Types and Impacts of XSS
- **Reflected XSS:** User input is returned immediately via a URL or parameter.
- **Stored XSS:** Payload is saved on the server and delivered to other users.
- **DOM-Based XSS:** Vulnerability exists entirely in client-side code/JavaScript.
- The main risk is what can be done with the injected code, not just showing alerts.

## Self XSS vs Real Reflected XSS
- **Self XSS:** The vulnerability only affects the user who enters the payload; it cannot be exploited through a crafted URL targeting others.
- **Real Reflected XSS:** Can be exploited by sending a single crafted URL to a victim—execution occurs when the link is clicked.
- **Test:** If the attack works with just a single URL click, it’s a genuine reflected XSS. If more steps are needed (manual copy-paste), it’s “self XSS” and not worth reporting.

## Finding and Exploiting Reflected XSS

### 1. Identify Reflected Inputs
- Look for URL parameters and search fields where input is returned on the page.

### 2. Basic Testing
- Start by entering simple payloads like `<script>alert(1)</script>`, but expect most real applications to block these.
- Use the browser’s developer tools to inspect how the payload is rendered.

### 3. Analyze Filters and Outputs
- Check how the application processes and displays user input—are tags stripped, HTML encoded, or filtered?
- Understand filtering: try variations and encodings (e.g., case changes, HTML entity codes, URL encoding).

### 4. Bypass Techniques
- Use alternate tags if `<script>` is blocked. For example: `<img src=x onerror=alert(1)>`, or use SVG/event-handler payloads.
- If the payload 'alert' is blocked, assemble it using character codes.
- Reference lists like “Payloads All The Things” for a catalog of XSS bypass payloads.

### 5. DOM and JavaScript Analysis
- If reflection is happening via client-side JavaScript, inspect for unsafe sinks such as `innerHTML`, `document.write`, or dangerous Angular functions.
- Use browser debuggers to trace input from source to sink.
- Understanding the filtering/sanitization used (e.g., what libraries or functions block payloads) is crucial to crafting effective exploits.

## Practical Demonstration Example
- Use an application with a search bar.
    - Enter regular and HTML content; view the result in the browser’s inspector to see if input is interpreted as HTML.
    - Try various payloads, inspecting the outcome. If tags are allowed but scripts are filtered, transition to alternative vectors like image tags with `onerror`.
- Verify if the payload works via a single URL (indicator of real reflected XSS).

## Bug Bounty Strategy and Tips

- Prioritize programs with new or less-tested assets, frequent updates, or high interactivity/JavaScript use—competition is lower.
- Avoid super-competitive programs unless you have a unique angle.
- Focus on in-depth manual testing and code analysis, especially DOM XSS, where automation is less helpful.
- Learn how sanitization and JavaScript intricacies work to find and bypass defenses creatively.
- Only report XSS vulnerabilities that realistically impact other users (i.e., single-click exploits).

- [payloads All the things](https://github.com/swisskyrepo/PayloadsAllTheThings)
## Summary Checklist

- [x] Check if user input is reflected in responses.
- [x] Try basic XSS payloads and inspect behavior.
- [x] Analyze filtering and get creative with bypasses.
- [x] Study client-side JavaScript for DOM-XSS.
- [x] Confirm exploitability via a single URL click.
- [x] Target programs strategically; favor manual/creative analysis.

