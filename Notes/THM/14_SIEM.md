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

### Log Sources and Log ingestion
- Every device in the network generates some kind of log whenever an activity is performed on it,
   - like a user visting a wbsite , connecting to SSH, logging into his workstation , etc.

#### Windows Machine
- Windows records every event that can be viewed though the __Event viewer__ utility.
- it assigns a unique ID to each type of log activity , making it easy for the anlyst to examine and keep track of.
- To view event in windows env, type _Event Viewer_ in the search bar,
- and it  takes you to the tool where different logs are stored and can be viewed ,
- These logs from all windows enpoints are forwarded to the SIEM solution for monitoring and better visiblity.

#### Linux  Workstation
- Linux OS stores all the related logs , such as events , errors , warnings , etc.
- Which are then ingested into SIEM for continuous monitoring.
- Some of the Common locations where LInux store logs are:

  - __/var/log/httpd :__ Contains HTTP Request/Response and error logs.
  - __/var/log/cron :__ Events related to cron jobs are stored in this location.
  - __/var/log/auth.log and /var/log/secure :__ Stores authentication related logs.
  - __/var/log/kern :__ This fiile stores kernel related events.

#### Web Server
- it is important to keep an eye on all the requests/responses coming in and out of the webserver for any potential web attack attempt.
- in Linux, common location to write all apache related logs are __/var/log/apache__ or __/var/log/httpd.__

#### Log Ingestion
- All theses logs provide a wealth of information and can help in identifying securtiy issues.
- Each SIEM solution has its own way of ingesting the logs.
- Some common methods used by these SIEM solutions are explained below:

  1. Agent/Forwarder:
     - These SIEM provide a lightweight tool called an agent that gets installed in the Endpoint.
     - it is configured to capture all the important logs and send them to the SIEM server
  2. Syslog :
     - Syslog is widely used protocol to collect data from various systems like web servers, databases, etc., are sent real-time data to the centralized destination.
  3. Manual Upload :
     - Some SIEM solutions , like Splunk, ELK, etc., allow users to ingest offline data for quick analysis.
     - Once the data is ingested, it is normalized and made avaliable for analysis.
  4. Port-Forwarding :
     - SIEM solutions can also be configured to listedn on certain port,
     - and then the endpoints forward the data to the SIEM instance on the listening port.  
