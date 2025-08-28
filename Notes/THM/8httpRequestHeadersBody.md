# Request Headers
- Request Headers allow extra information to be conveyed to the web server about the request.
- some common headers are as follows:
## __Common Request Headers:__
- __Host__
- Example: `Host: tryhackme.com`
- Specifies the name of the web server the request is for.
- __User-Agent__
- `Ecample: `User-Agent: Mozilla/5.0`
- Shared information about the web browser the request is coming from.
- __Referer__
- `Referer: https://www.google.com/`
- Indicates the URL from which the request came from
- __Cookie__
- Example : 
 `Cookie: user_type=student;
    room=introtowebapplication;
    room_status=in_progress`
- information the web server previously asked the web browser to store is held in cookies
- __Content-Type__
- Example:
 `Content-Type: application/json`
 - Describes what type or format of data is in the request


# Request Body
- in Http requests such as POST and PUT,
- where data is sent to the web server as opposed to requested from the web server
- the data is located inside the HTTP request body.
- The formatting of the data can take many forms , 
- but some commoon ones are URL Encoded , Form Data , JSON , or XML.

  __URL Encoded (application.x-www-form-urlencoded)__
  - A format where data is structured in pairs of key and value where (key=value)
  - Multiple pairs are spearated by an (&) symbol , such as key=value1&key2=value2
  - Special characters are percent- encoded
  - __Example:__
    
        POST /upload HTTP/1.1
        Host: tryhackme.com
        User-Agent: Mozilla/5.0
        Content-Length: 33
    
        nam=Aleksandra&age=27&county=US
    
  __Form Data (multipart/form-data)__
  - Allows multiple data blocks to be sent where each block is separated by a boundary string.
  - The boundary string is the defined header of the request itself
  - This type of formatting can be used to send binary data , such as when uploading files or images to a web server
  - __Example__
  
        POST /upload HTTP/1.1
          Host: tryhackme.com
          User-Agent: Mozilla/5.0
          Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW 

          ----WebKitFormBoundary7MA4YWxkTrZu0gW
          Content-Disposition: form-data; name="username"

          aleksandra
          ----WebKitFormBoundary7MA4YWxkTrZu0gW
          Content-Disposition: form-data; name="profile_pic"; filename="aleksandra.jpg"
          Content-Type: image/jpeg

          [Binary Data Here representing the image]
          ----WebKitFormBoundary7MA4YWxkTrZu0gW--
         
  __JSON (application/json)__
  - in this format, the data can be sent using the JSON(JavaScript Object Notation) structure.
  - Data is formatted in pairs of name: value.Multiple pairs are separated by commons , all contained within curly braces {}/
  - __Example:__
  
          POST /api/user HTTP/1.1
          Host: tryhackme.com
          User-Agent: Mozilla/5.0
          Content-Type: application/json
          Content-Length: 62

          {
              "name": "Aleksandra",
              "age": 27,
              "country": "US"
          }
    
    __XML (application/xml):__
    - in XML formatting data is structured inside labls called tags,which have an opening and closing.
    - These labels can be nested within each other
    - you can see in the example below the opening and closing of the tags to send details about a user called Aleksandra.
    - __Example__
    
          POST /api/user HTTP/1.1
          Host: tryhackme.com
          User-Agent: Mozilla/5.0
          Content-Type: application/xml
          Content-Length: 124

          <user>
              <name>Aleksandra</name>
              <age>27</age>
              <country>US</country>
          </user>
        

  
## __Type of communication Mode:__
http , cloudfire free ssl certification
### __web sockets :__
- tonnel between server and client , if server put smth on tunnel client get this,if client put smth server
### __subscribal patten :__
- like mail you get with unscubscibe button
### __gRPC (google Remote  processor call) :__ 
- is validate data befoer send ,
- if it's not proper then don't send that server to save api call (cost) and for security
