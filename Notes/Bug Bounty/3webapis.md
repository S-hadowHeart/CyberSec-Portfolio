# what is an API?
- A type of web applications that is designed for other applications to interact with it rather than humans
- This might be intentionally as a way to provide 3rd party apps:
  - E.g. Twitter developer API
- or just for a single application
- Developers can write a single API and resue that code for a mobile app, a desktop app, a website etc...
  - Write code once
 
  ## Introducting JSON
  - JSON is a way to represent data in a text format
  - it starts with a curly brace {, and ends with one
  - JSON contains objects which are denoted with {} and array/lists []
  - Within these you have key-value pairs which store the ata
  - it's important to become familiar with reading JSON so take the time to learn it
 
  ## Types of API
  ### RESTful
  - RESTful APIs are really easy to spot
    - They have a defined structure with realtes to CRUD funcitionality
  - You can easy predict new endpoints simply by knowing an application
     - Eg: if youtube's API has something like GET/video/1
     - you  can assume DELETE /video/1 also exists
     - And that if YouTube has videos maybe GET/comment/1 exists for comments
  - They are widely used, however some of the endpoints may be more custom
     - Eg: DELETE /posts/1 vs POST/posts/1/delete
  - They Usally return JSON
  - RESETful APIs can be challenging to enumerate , we need to guess the resource names
  - Common resource names
    - using a list of common RESTful endpoints or a wordlist
    - if you can find a more tailored word list , start there
  - Custom resource names
    - Knowing the functionality of the app curate some likely endpoints
    - Does the API powers a forum? try post, reply
    - API wordlist
      - Kiterunner
      - FFUF + API wordlist
     
  ### Clicking Buttons
  - The best way i discover APIs is clicking on buttons
  - E.g. Zoom -> meetings app?
  - well
     - Third party apps via their store
     - Zoom rooms allows for room booking
     - Zoom whiteboard
  - All of these are going to use the API and can be a Victim of API issues

### API Security Issues:
- OWASP API Top 10
   - API1 Broken object LEvel Authorization
   - API2 Broken Authentication
   - API3 Broken object property Level Authorization
   - API4 unrestricted Resource Consumption
   - API5 Broken Function LEvel Authorization
   - API6 Unrestricted Access to sensitive Business Flows
   - API7 server Side Request Forgery
   - API8 Security Misconfiguration
   - API9 improper Inventory Management
   - API10 Unsafe consumption of APIs

### Access Control 3 Diffrent ways
- Object
  - Begin able to edit a object that does not belong to you
  - usually because any authorisation check is missing
  - Really common in generated APIs
- Property
  - Think things that require additional information
  - Need current password to change your password
  - Usually you see this as info disclosure
- Permissions
  - Common with complex hirerarchies or tenancy applications
  - Can be horizontal AND vertical

### The Cookie Trick - Authentication Check
- Create an account/log in
- Perform a bunch of requests
- Go to the request and remove the cookie
  - Effectively treating the requests as if they came from no particular user
- Check and see if they're caused something to happen to our account

### The cookie Trick - Authorisation check
- Create an account/log in (Account A)
- Perform a bunch of requests
- Create an account/log in (Account B)
- Go to see if they've caused something to happen to account A rather than B
  - __This Is Importnt if you can affect B with B's Cookie this is not A vulnerability you are logged in as B__

### Information Disclosure:
 - PII (personal identifiable information)
 - Access control isses that allow read access
 - Error Messages/ software Disclosure
 - Comments,API keys etc...
 - more techniques

### Integrations and Business Logic
- integrations are great places to find business logic issues
- often between 3r party APIs
  - Or systems e.g. payments  vs ecommerce
  - Difficult to give advice on finding them
  - if you see any complex flows , can you break them?
  #### Developer APIs
  - Example reddit with full documentation
  - 
  #### Stages of Hacking
  - Find Endpoints : Recon is probably one of the most challenging things about API hacking but you don't need to find everything
  - Test for issues between API UI : Don't overcomplicate things intially, still do limus tests for XSS, SQLi etc..
  - Test for API specific bugs : ALWAYS test an API for access control issues - they are by far the most common API bugs
  - Escalate : APIs are great places to find and use bug chains account takeovers are the 'easiest' critical vulnerabilities to find.
  - Batched
    - common in mobile applications
  - GraphQL
  - SOAP
    - primary use in legacy applications
   
  ### Xss, SQLI , cSRF and other acronyms
  - if you take nothing else from this talk take this
    - PAIs are 
  
  
