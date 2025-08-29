# Http Status
- When you interact with a web application ,
- the server sends back an HTTP response to let you know whether your request was successful or something went wrong.
- These responses include a status code and short explanation (called the reason Phrase)
- that give insight into how the server handled your request

## Status Line:
- The first line in every HTTP response is called the __status Line__.
- it gives you three key pieces of information:
  1. __HTTP version :__ This tells you which version of HTTP is being used.
  2. __Status Code :__ A three-digit number showing the outcome of your request.
  3. __Reason pahrase :__ A short message explaining the staus code in humna-readable terms

### Status Codes and Reason Phrases :
- __Status code__ is the number that tells you if the request succeeded  or failed, while the Reason phrase explains what happened.
- These Codes fall into five main categories:
- __Informational Responses (100-199) :__
  - These codes mean the server has received part of the request and is waiting for the _rest_(representational state transfer is software architectural style that was created to guide the design and development of the architecture for world wide web)
  - it's a "keep going" signal
- __Successful Responses (200-299) :__
- These codes mean everything worked as expected.
- The server processed the request and send back the requested data.
- __Redirection Messages (300-399) :__
- These codes tell you that the resource you requested has moved to a different location , usally providing the new URL.
- __Client Error Responses (400-499) :__
- These codes indicate a problem with the request.
- Maybe the URL is wrong , or you're missing some requeired info , like authentication.
- __server Error Responses (500-599) :__
- These codes mean the server encountered an error while trying to fulfil the request.
- These are usally server-side issues and not the client's fault.

### CCommon Staus codes:
- Most frequently seen status code
#### 100 (continue) :
- The server got the first part of the request and is ready for the rest
#### 200 (ok) :
- The request was successful , and the server is sending back the requested resource
#### 301 (Moved permanently) :
- The resource you're requesting has been permanently moved to a new URL.
- use the new URL from now on.
#### 404 (NOt Found) : 
- The server couldn't find the resource at the given URL.
- Double-check that you've got the right address.
#### 500 (internal server error)
- something went wrong on the server's end and it couldn't process your request
