# Type of communication 
## unicast Communication (1:1)
- Transmitting the data from one computer to another computer is called as unicast communication
- it is one to one transmission
  - Note :
    - in unicast communication both source and destination can be presont in the same network or diffrent netwokr 
## Broadcast communication (1:All)
- Two Type
  ### Limited Broadcasting :
    - Transmiting data from one computer to all other computer in the same network is called as Limited Broadcasting
    - D.I.P will always `255.255.255.255` called Limited Broadcast Address
    - Limited broadcast Address can't be used as a source IP Address(S.I.P)
  ### Direct Broadcasting :
    - Transmiting data from one computer to all other computer in the diffrent network is called as Direct Broadcasting
    - D.I.P will x.255.255.255
    - Note:
      - when ever we have all 1's in HID part of any IP address, that IP address reperesent the Direct broadcast address so this is the reason we can't assign this IP address to any host
      - Direct Broadcast Address can't be used as a source ip address (S.I.P)
      - Direct Broadcast Address will Always be used as a distination Ip Address (D.I.P)
  - No Brodcast in Class D and E
 
## __Network Masks:__
- A network mask helps you to know which portion of the address identifies the network-id and which portion of the address identifies the host-id.
- Class A,B and C networks have default masks,
- also known as natural masks as , shown here :
  - Class A : 255.0.0.0
  - Class B : 255.255.0.0
  - Class C : 255.255.255.0
- Note:
  - in the network mask no of 1's indicate NID part and
  - No of 0's indicate HID part
  - if you do bitwise And of ip add and netowrk mask you will get network id
  - or just 0 all in host id , you will get network id. xD

## Multicast communication (1:many)


