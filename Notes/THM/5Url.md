# UNiform Resource Locator (URL) :
- URL is a web address that les you access all kinds of onlince content
- whether it's a webpage,a video , a photo , or other mdedia.
- It's guides your browser to the right place on the Internet.
## Anatomy of URL
<img width="1140" height="270" alt="url" src="https://github.com/user-attachments/assets/b04385a7-89c8-426c-92ed-83116b365118" />
### Scheme
- is protocol used to access the website.
- The most common are http and https
  - https is more secure cuz it encrypts the connection ,
  - which is why browsers and cyber securtiy experts reccomend it
  - webstier often enforce Https for added protection
### User
 - Some URLs can include usre's login details(usally a username) for sites that require authentication.
 - This happens mostly in URLs that need credentials to access certain resources
   - However it's rare nowadays cuz putting login details in the URL isn't very safe
   - it can expose sensitive info , which is security risk
### Host/Domain
- domain is the most important part of URL cuz it's tells you which website you are accessing
- Every domain name has to be unique and is registered through domain registrars.
- From a security standpoint , look for domain name that almost like real ones but have small differnces (this is called __typosquatting__).
- These fake domain are often used in phishing attacks to trick people into giving up sensitive info
### port
- port number helps direct your browser to the right service on the web server.
- it's like telling the server which doorway to use for communication.
- Portnumbers range from 1 to 65535
- but most common are 80 for Http and 443 for https
### Path
- The path points to the specific file or page on the server that you're trying to acccess
- shows the browser where to go.
- websites need to secure these paths to make sure only authorised users can access sensitive resources.
### Query string
- is part of the URL that starts with question mark (?).
- it's often used for things like search terms of form inputs.
- Since user can modify these query strings ,
- it's important to handle them securely to pervent attacks like injections ,
- where malicious code could be added
### Fragment
- starts with hash symbol (#)
- Helps point to specific section of webpage like jumping directly to particular heading or table
- users can modify this too ,  so like with query strings
- it's important to check and clean up any data here to avoid issues like injection attacks.

