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
    -  `sU` : UDP Scans
      - lack of acknowledgement
      - makes udp significantly more diffcult(and much slower) to scan.
      - when packet is sent to an open UDP port , there should be no response.
      - when this happens Nmap refers to port as begin open|filtered.
      - if it gets a USP responce(which is very unsual) , then the port is marked as open.
      - More commonly no response , in which case the request is sent a second time as a double-check. if no responce then port ise market open|filtered and Nmap moves on.
      - __When packet is sent to closed UDP port__
        - Target should respond with an ICMP(ping) packet containing a msg that the port is unreachable.
  - Less common port Scan Type:
    - `sN` : TCP Null Scans
      - when TCP request is sent with no flags set at all.
      - As per the RFC, the target host should respond with RST if the port is closed.
    - `sF` : TCP FIN Scans
      - insted of sending a completely empty packet , a request is sent with FIN flag
      - NMAP expects a RST if the port is closed
    - `sX` : TCP Xmas Scans
      - send a malformed TCP packet and expects a RST response for closed ports.
      - it's referred to as an xmas scan as the flags that it sets (PSH, URG and FIN) give it the appearance of blinking christmas tree when viwed as a packet capture in wireshark
      - if port open no response to malformed packet
      - filtered of target has responded with ICMP unreachable packet
    - All threee is interlinked

_it's also worth noting that while RFC 793 mandates that network hosts respond to malformed packets with a RST TCP packet for closed ports, and don't respond at all for open ports; this is not always the case in practice. In particular Microsoft Windows (and a lot of Cisco network devices) are known to respond with a RST to any malformed TCP packet -- regardless of whether the port is actually open or not. This results in all ports showing up as being closed._

RFC - A Request for Comments (RFC) is a publication in a series from the principal technical development and standards-setting bodies for the Internet, most prominently the Internet Engineering Task Force (IETF).
  
