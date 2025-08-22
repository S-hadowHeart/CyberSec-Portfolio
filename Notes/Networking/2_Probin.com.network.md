# PROBLEMS IN COMPUTER NETWORK
###### Classful Addressing Disadvantages
- Class A
    - 2^24 ip in one netowkr
- Class B
    - 2^16 ip in one network
- Class C
    - 2^8 ip in one network

## Examples
__Ex 1 : Organization X need 2^20 Ip addresses__
- IF we give Class A network.
- How many ip waste:
    - 2^24 - 2^20
    - 15M (15,728,640 ip wiil Waste)
__Ex 2: ORganization Y need 2^10 Ip addresses__
- IF we give Class B network.
- waste of IP : 63K (64,512)

__EX 3: Organization Z need 2^7 IP addresses__
- IF we give class C Network
- waste of IP: 128 ip

## Problems in Computer Network
1. Communication Problem
2. Identification Problem
3. Connection Problem

### 1. Communication Probelem 
- Language ? should same language 
- Meaning  ? means should understable
- Response ? reciver should reply

#### Solution:
-  Communication Problem can be solved by using Protocols
- A protocol is a set of rules that govern data communication
- Protocol defines:
    - What is communicated?
    - How it is communicated?
    - When it is communicated?
      
- Key Elements  of Protocols
    1. Syntax :
         - The term Synta refers to the structure of data, meaning the order in which they are presented
         - __Example:__
             - Some protocol might accept first 8 bit of data to be the Address of sender.
             - the second 8 bit to be the address of reciver
             - And rest of the stream to be the message itself.\
               
    2. Semantics
         - The word semantics refers to the measning of each section of bits.
                   
    3. Timing
         - The term timing refers of two characteristics when data should be send and How fast they can be sent
         - __Example:__
           - If a sender produce data at 100 Mbps
           - but reciver can process data at any 1 mbps ,
           - the transmission will overload the recevier and some data will be lost

### 2. Identification Problem
- To send a packet from source to destination we need 3 identification steps
    1. Identify the Network
       - Example Class-A have 1 - 126 Network , how we will identify  each Network ?
       - Note:
           - When ever we have all 0's in HID part of any IP Address ,
           - that ip address represent the NID of entire network
           - this is the reason we can't assign this IP address to any host(computer).
       - __SO, How you will identify Network?__
           1. Identify Class : that you can by looking first some bit
           2. Make all bit 0 in Host id
           3. That ip you get is your Netowork ^^)
       - Solutions:
           1. Soultion for identification of network is IP Address or logical Address.
             - Now we get destination IP using DNS 
           2. Solution For Identification of Host within the network is physical Address or MAC Address.
             - Given an ip Address we get MAC address using ARP (Addresse Resolution protocol) 
           3. Solution For Identification of process within the Host is Port Number.   

    2. Identify the host with in the network i.e. among all computer one computer is identified.
       - host means phycial Address or MAC Address (can't change)
       - IP is Logical Address (can be change)
       - __We Have Protocol called ARP (Address Resolution Protocol)__
           - ARP Request: |IP Address = x.x.x.x , MAC Address = ?|
               - ARP request is Broadcasting
               - ARP reply is Unicasting
               - Example : Professor when to find one student from 400 student , they will just announce name and say stand up 👀

    3. Identify the process with in the Host.
       - Now we have network and also we found mac means computer
         - but in computer there are many process running that is identify by ports (toatl 16 bit)
           - Range 0 to 65,535
           - 0 to 1023 --> well known port no assigned and control by IANA (Police🚨 100 , 🚑 --> 108 same way in computer network)
             - Example : 
               - SMTP --> 25
               - HTTP --> 80
               - FTP --> 20,21
               - DNS --> 53
               - POP --> 101
               - IMAP  --> 143
           - Example : IF your friend send msg in mail and you got in whatsapp , ofcos no that why we need to identify port 🫠 


### 3. Connection Problem
  - There are Various Ways to connect the System
      - Bus  Topology
      - Ring Topology
      - Mesh Topology
      - Tree Topology
      - Star Topology

    
  
