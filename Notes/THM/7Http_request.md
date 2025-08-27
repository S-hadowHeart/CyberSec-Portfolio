# HTTP request
- is  what a user sends to web server to interact with a web application and make something happen
- since these requests are often the first point of contact between the usre and the web server , knowing how they work is super important- expecially if you're into cyber security
<img width="1140" height="600" alt="http" src="https://github.com/user-attachments/assets/ec3c1882-d7cc-4e15-a39b-315b566853ec" />

  ## Request Line(start line)
  - tells the server what kind of request it dealing with what kind of reqest it's deling with.
  - it has three main parts:
    - The _HTTP method_,
    - The _URL path_,
    - The _HTTP version_
  - Example : `METHOD /path HTTP/version

## HTTP Methods
- tells the server what action the user wants to perfrom on the resource identified by the URL path
### some common methods and their possible security issue:
- __GET__ :
- used to fetch data from server without makeing any changes.
- Avoid putting sensitive info like tokens or passwords i GET requests since they can show up ads plaintext
### __POST:__ 
- sends data the server , usually to create or update something
- Always validate and clean the input to avoid attacks like SQL injection or XSS
### __PUT:__
- Replace or updates something o nthe server .
- Make sure the user authorised to make changes befoer accepting the request
### __DELETE:__
- Removes something from the server
- Just like with PUT make sure only authorised users can delete resources
- Besides these common methods, there are a few othere userd in specific cases:
### __PATCH:__
- Updates part of resource
- useful for making small changes without replacing the whole thing,
- but always validate the data to avoid inconsistencies
### __HEAD:__
- works like GET but only retrieve headers ,
- not the full content
- it's handy for checking metadata without downloading the full response
### __OPTIONS:__
- Tells you what methods are avaliable for specific resource,
- helping clients understand what they can do with the server.
### __TRACE:__
- Similar to OPTIONS,
- it shows which methods are allowed ,
- often for debugging.
- Many servers disable it for security resons.
### __CONNECT:__
- used to create secure connection like HTTPS.
- it's not as common but is critical for encrypted communication
- Each of these methods has its own set of security rules
- Example:
  - PATCH requests should be validated to avoid inconsistencies,
  - and options and Trace should be turned off if not needed to avoid possible security risks.

## URL Path
- it's tell server where to find the resource the user is asking for
- For instance, in the URL `https://thm.com/api/user123`, the path `/api/users/123` identifies a specific user
- Attackers often try to manipulate the URL path to exploit vulnerabilities , so it's crucial to :
  - Validate the URL path to prevent unauthorised access
  - sanitise the path to avoid injection attacks
  - Protect sensitive data by conducting privacy and risk assessments

## HTTP Version
- shows the protocol version used to communicate between the client and server.
- Here's quick rundown of the most common ones:
### HTTP/0.9 (1991)
- The first version, only supported GET requests
### HTTP/1.0 (1996)
- Added headers and better support for different types of content , improving caching.
### HTTP/1.1 (1997)
- Brought persistent connections , chunked transfer encoding and better caching.
- it's still widely used today
### HTTP/2 (2015)
- introduced features like multiplexing, header compression , and prioritisation for faster performance.
### HTTp/3 (2022)
- BUilit on HTTP/2, but uses a new protocol (QUIC) for quicker and more secure connections.

- Although HTTP/2 and HTTP/3 offer better speed and security ,
- many systems still use HTTP/1.1 cuz it's well-supported and works with most existing setups.
- However upgrading to HTTP/2 or HTTP/3 can provide significant performance and security improvements as more systems adopt them
