# Brup Suite

## Proxy Module:
- gives you a direct view into how your target applications work "under the hood".
- it's operates as a web proxy server and sits as a man-in-middle between your browser and destination web servers.
- This lets you intercept , inspecept, inspect and modify the raw traffic passing in both directions
  - proxy listener :
    - defult burp on port 8080 of your ipv4 lookback interface
- __set proxy in browser of brup__
- intercept packet

## scope and spider
- add scope using right click on packet (so it will show in target , using that you can get structure of website)
- then you can send to spider so you will get dir , site map , files , url , images etc etc
- __spider also know as Crawl__
  - for limit you can choice
    - This time taken
    - Then number of unique locations discoverd. A locations represents asdistinct unit of content or functionality baced on the chosen crawl stategy.
    - The number of HTTP requests that are made

## Scanner
  - you can scan only one page , insite of whole website
  - you can see common issue(varnablity) and read about that from here

## Community vs Professional vs Enterprise
 - scanner module,web vulnerbility,advanced manuaal tools not avalible in compunity
 - scheduled & repeat scans , unlimted scalbility , CI integration not avalible in professional
 - you can chek diffrent from internet

## intruder
 - tool that automating customized attacks against web applications
 - it is extremly powerful and configurable, and can be used to perform a huge range of tasks, from simple brute-force guessing of web directories through to active exploitation of complex blind SQL injection vulnerablities
 - it's modify http request (called the "base request")
 - categories where commonly use is :
   - Enumerating identifiers
   - Harvesting useful data
   - Fuzzing of vulnerablities (like sql inhection , cross-site scripting and file path traversal)
   - also you can do DOS attack

## Brute-Force Attack using Burp suite intruder
 - example you have login form and you have list of usernames and passwords that you want to try to login
 - step to do :
   - capture request
   - right click send to intruder
   - select attack type cluster bomb , click on payloads
   - you can add username , passoword list etc. ..
   - then click on start attack on right corner
   - also you can change threshold etc from options
  
## Repeater Module
  - without open browser you can get response..
  - simple tool for manually manipulating and reissuing individual HTTP request
  - and analysic responces


be back after lunch ^^)
