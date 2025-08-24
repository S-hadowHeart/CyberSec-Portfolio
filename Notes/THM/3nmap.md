# NMAP

- When computer runs a network service, ,it opens a networking construct called a "port" to receive the connections.
- Total ports 65535 in computer
- many of these are registered as standard ports (total 1024)

- _Nmap_
  - "Network Mapper"
  - open-source tool used for network discovery and security auditing.
  - assists in the exploration of network hosts and services,providing info about open ports, os and other details.
  - can be usted perform many diffrent kinds of port scan
  - basic theory is this : NMAP will connect to each port of the target in rurn Depending on how the port responds, it can determind as being open,closed , or filtered (usually by a firewall)
  - after that we can know running services on open port

  - __nmap -h__ : to see all commands
  - Basic scan Tyeps:
    - `-sT` : Tcp Connect Scans
      - use Three-way handshake
      - if target send `SYN/ACK` then port noted as `open`
      - if target send `RST`(Rest) then port noted as `closed`
      - what if port is open but hidden behide a firewall?
        - many firewalls are config to simply drop incoming pakets
        - NMAP sends a TCP SYN request, and receives nothing back
        - This indicates that the port is being protected by a firewall and thus the port is considerd to be `filtered`
          - It's very easy to config firewall to respond with RST TCP packet
          - Example in IPtables for Linux:
            - `iptables -I INPUT -p tcp --dport <port> -j REJECT --reject with tcp-rest`
            - That make things extremely difficult even we find any way it will not accurate
    -  `sS` : SYN "Half-open" Scans
      - also known as "Half-open" scans or "Stealth" scans
   
      - 
    -  `sU` : UDP Scans

  - Less common port Scan Type:
    - `sN` : TCP Null Scans
    - `sF` : TCP FIN Scans
    - `sX` : TCP Xmas Scans
   
    

  
