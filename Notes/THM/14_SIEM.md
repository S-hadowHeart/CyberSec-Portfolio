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

## Why SIEM 
- is used to provide correlation on the collected data to detect threats.
- Once a threat is detected , or a certain threshold is crossed , an alert is raised.
- This alert enables the analysts to take suitable actions based on the investigation.
- SIEM plays an important role in Cyber security domain and helps detect and protect against the lastest threats in timely manner.
- it provides good visiblity of what's happening within the network infrastructure.

### SIEM Capabilities
- SIEM is one major component of a security Operations Center(SOC) ecosystem,
- SIEM starts by collecting logs and examining if any event/flow has matched the condition set in the rule or crossed a certain threshold

- Some of the common capabilities of SIEM are:
  - Correlation between events from diffrent log sources.
  - provide visibility on both Host-centric and Network-centric activities.
  - Allow analysts to investigate the latest threats and timely responses.
  - Hunt for threats that are detected by the rules in place.
 
### SOC Analyst Responsiblities
- SOC analysts utilize SIEM solutions in order to have better visibility of what happening within the network.
  - Monitoring and Investigating.
  - identifying False positives
  - Tuning Rules which are causing the noise or False positives
  - Reporting and Compliance.
  - Identifying blind spots in the network visiblity and covering them.

## Analysing Logs and Alerts
- SIEM tool gets all the security-related logs ingested through agents, port forwarding , etc.
- Once the logs are ingested,SIEM looks for unwanted behavior or suspicious pattern within the logs with the help of the conditions set in the rules by the analysts.
- if the condition is met,
  - a rule gets trigged, and the incident is investigated.

### Dashboard
- Dashboards are the most important components of any SIEM.
- SIEM presents the data for analysis after being normalized and ingested.
- The summary of these analyses is presented in the form of actionable insights with the help of multiple dashboards.
- Each SIEM solution comes with some default dashboards and provides an option for custom Dashboard creation.
- Some of the information that can be found in a dashboard are:
  - Alert Highlights
  - System Notification
  - Health Alert
  - List of Failed Login Attempts
  - Events ingested Count
  - Rules triggered
  - Top Domains Visited
 
- An Example of a Default dashboard in __Qradar SIEM__ is shown below:
  <img width="1904" height="977" alt="image" src="https://github.com/user-attachments/assets/27910995-7f07-4aa6-a740-6d4b5228ee77" />

  ### Corelation Rules
  - Correlation rules play an important role in the timely detection of threats allowing analysts to take action on time.
  - Cirrekatuib rykes are prety much logical expressions set o be triggered.
  - A few examples of correlation rules are:
 
    - If a User gets 5 failed Login Attempts in 10 seconds - Raise an alert for _Multiple Failed Login Attempts_
    - if login is successful after multiple failed login attemps - Raise an alert for _Successful Login After multiple Login Attempts_
    - A rule is set to alert every time a user plugs in a USB (Useful if USB is restricted as per the company policy)
    - If outbound traffic is > 25 MB - Raise an alert to potential Data exfiltration Attempt(Usally it depends on the company policy)
### How a correlation Rule is created
- To explain how the rule works , consider the following Eventlog use cases:
__Use-Case 1 :__
  - Adversaries tend to remove the logs during the post-exploitation phase to remove their tracks.
  - A unique Event ID __104__ is logged every time a user tries to remove or clear event logs.
  - To create rule based on this activity, we can set the condition as follows:
  - __Rule:__ if the Log source is winEventLog __AND__ EventID is __104__ - Trigger an alert __Event Log Cleared__
- __Use case 2: __
  - Adversaries use commands like __whoami__ after the exploitation/privilege escalation phase.
  - The following Fields will be helpful to include in the rule.
    - Log source: Identify the log source capturing the event logs
    - Event ID: which Event ID is associated with process Ececution activity? in this case event id 4688 will be helpful.
    - NewProcessName: which process name will be helpful include in the rule?
    - __Rule :__ if log source is winEventLog __AND__ EventCode is __4688__, and New ProcessName contains __whoami__ then Trigger an ALERT __WHOAMI command Execution DETECTED__

### Alert Investigation:
- when monitoring SIEM, analysts spend most of their time on dashboards as it displays various key details about the network in very summarized way.
- Once an alert is triggered, the events/flows associated with the alert are examined , and the rule is checked to see which conditions are met.
- Based on the Investigation , the analyst determines if it's True or False positive.
- Some of the actions that are performed after the analysis are:
  - Alert is False Alarm. it may require tuning the rule to avoid similar False positives from occurring again
  - Alert is True Positive. perform futher investigation
  - Contact the asset owner to inquire about activity
  - Suspicious activity is confirmed. Isolate the infected host
  - Block the suspicous IP
  - 
