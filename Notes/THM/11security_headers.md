# Security Headers
- help improve the overall security of the web application by providing mitigations against attacks like `Cross-site Scripting`(XSS),clickjacking, and others
- we will now dig deeper into the following security headers:
  - Content-Security-Policy (CSP)
  - Strict-Transport-Security (HSTS)
  - X-Content-Type-Options
  - Referrer-Policy
- __security headers of any webstie__
  - `https://securityheaders.io`
## Content-Security-Policy (CSP)
- A CSP header is an additional security layer that can help mitigate against common attacks like Cross-Site Scripting (XSS).
- Malicious code could be hosted on a separate website or domain and injected into the vulnerable website.
- A CSP provides a way for administrators to say what domains or sources are considered safe and provides a layer of mitigation to such attacks.

- within the header itself , you may see properties such as `default-src` or `script-src` defined and many more.

## Example CSP header:
`Content-Security-Policy: default-src 'self'; script-src 'self'`
`https://cdn.thm.com;style-src 'self'`
we see the use of : 
- __default-src :__
  - which specifies the default policy of self,
  - which means only the current website
- __script-src :__
  - which specifics the policy for where scripts can be loaded from , which is self along with scripts hosted on `https://cdn.thm.com`
- __style-src :__
  - which specifies the policy for where style CSS style sheets can be loaded from the current website(self)
## Strict-Transport-Security (HSTS)
- The HSTS header ensures that web browsers will always connect over HTTPS.
- Let's look at an example of HSTS:
  `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
  - breakdown of the Example HSTS header by directive:
    - __max-age__
      - This is the expiry time in seconds for this setting
    - __includeSubDomains__
      - An optional setting that instrucs the browser to also apply this setting to all subdomains.
    - __preload__
      - This optional setting allows the webstie to be included in preload lists.
      - Browsers can use preload lists to enforce HSTS before even having their first visit to a website.
### Referrer-Policy
- This header controls the amount of information sent to the destination web server when a user is redirected from the source web server,
- such as when they click a hyperlink.
- The header is avaliable to allow a web administrator to control what information is shared.
- Here are some examples of Referrer-Policy:

      Referrer-Policy: no-referrer
      Referrer-Policy: same-origin
      Referrer-Policy: strict-origin
      Referrer-Policy: strict-origin-when-cross-origin
- Here's a breakdown of the Referrer-policy header by directives:
  - __no-referrer :__
    - This completely disables any information begin sent about the referrer
  - __same-origin :__
    - This policy will only send referrer information when the destination is part of the same origin.
    - This is helpful when you want referrer information passed when hyperlinks are within the same website but not outside to external websites
  - __strict-origin :__
    - This policy only sends the referrer as the origin when the protocol stays the same.
    - So, a referrer is sent when an HTTPS connection goes to another HTTPS connection.
  - __strict-origin-when-cross-origin :__
    - This is smilar  to strict-origin except for same-origin requests,
    - where it sends the full URL path in the origin header.
      
