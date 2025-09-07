# What is SIEM 
- SIEM stands for __Security information and Event Management System__
- _it is a tool that collects data from various endpoints/network devices across the netwrok,stores them at centralized place,and performs correlation on them._

## Network visiblity through SIEM
- each network component can have one or more log sources generating diffrent logs.
- One Example could be setting up Sysmon along with Windows Event logs to have better visibility of windows Endpoint.
- We can divide our network log souce into two logical parts:

### Host-Centric Log Sources
- These are log sources that capture events  events that occurred within or related to the host.
- Some log sources that generate host-centric logs are windows Event logs, sysmon , Osquery , etc.
- some examples to host-centric logs are:
   - A user accessing a file
   - A user attempting to authenticate.
   - A process Executino Activity
   - A process adding/editing/deleting a registry key or value.
   - Powershell execution
### Network- Centric Log Sources
- Network-related logs are generated when the hosts communicate with each other or access the internet to visit a wbesite.
- Some network-based protocols are SSH,VPN, HTTP/s,FTP, etc.
- Example of such events are:
   - SSH connection
   - A file being accessed via FTP
   - Web traffic
   - A user accessing Company's resources through VPN
   - network file sharing Activity

<img width="501" height="542" alt="image" src="https://github.com/user-attachments/assets/cbb2ca33-7849-4bd3-b147-765e23ad9d2d" />

 
## Importance of SIEM
- As all these devices generate hundreds of events per second,
- examing the imglogs on each device one by one in case of any incident can be a tedious task
- That is one of the Advantages of having SIEM solution in place.
- it not only takes logs from various source in real-time but also provides the abilty to correlate between events , search trhough the logs , investingate incidents and respond promptly.
- __some key features provides by SIEM are:__
  - Real-time log ingestion
  - Alerting against abnormal activites
  - 24/7 Monitoring and visibility
  - Protection against the latest threats through early detection
  - Data insights and visualiazation
  - Ability to investigate past incidents
  - 
   - A user accessing companny's resources through VPN
   - Network file sharing Activity

### Importance of SIEM
- Now that 
