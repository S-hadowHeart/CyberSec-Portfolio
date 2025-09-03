# SOC (Security Operations Center)
- is dedicated facility operated by specialized security team.
- This team aims to continuously monitor an organization's network and resources and identify suspicious activity to prevent damage.
- This team works 24 hours a day , seven days a week

## Purpose and Components
- The main Focus of team is to keep Detection and Response intact.
- Tthe team has some resources avaliable in the form of security solutions that help them achieve this
- These solutionos integrate the whole company's network and all the system to monitor them from one centralized loaction.
- Continuous monitoring is required to detect and respond to any security incident.

## Detection
- __Detect vulnerabilities:__
  - A vulnerability is a weakness that an attacker can exploit to carry out things beyond their permission level.
  - A vulnerabllity might be discovered in any device's software (operating system and programs), such as server or computer.
  - For instance, the SOC might discover a set of MS Windows computers that must be patched against a specific publisged vulnerability.
  - Strictly speaking , vulnerabilities are not necessarily the SOC's responsibility; however , unfixed vulnerabilities affect the security level of entire company.

- __Detect unauthorized activity:__
  - Consider the case where an attaacker discovered the username and password of one of the employees and used them to log in to the company system.
  - it is crucial to detect this kind of unauthorized activity quickly befoer it causes any damage.
  - Many clues , such as geographix location , can help us detect this.

- __Detect policy violations:__
  - A security policy is a set of rules and procedures created to help protect a company against security threats and ensure compliance.
  - what is considered a violation would vary from company to company;;;
  - example include downloading pirated media files and sending confidential company files insecurely.
 
- __Detect intrusions:__
  - intrusions refer to unauthorized access to system and networks.
  - One scenario would be an attacker successfully exploiting our web application.
  - Another would be a user visiting a malicious site and getting their computer infected.

## Response
- __support with incident response:__
- once an incident is detected , certain steps are taken to response includes minimizing its impact and performing the root cause analysis of the incident.
- The SOC team also helps the incident response team carry out these steps.

- There are three pillars of a SOC
- with all these pillars , a SOC team becomes mature and efficiently detects and responds to differentt incidents.
- These pillars are People , Process and Technology.

- __People, Process and Technology__ coxist in a SOC environment.
- A team of professional individulas working on state-of-the-art security tools in the presence of proper processes
- is what makes a mature SOC environment.


### People: 
- Regardless of the evolutino of automating the majority of security tasks,the People in a SOC will always be important.
- A security solutinon can generate numerous red falgs in a SOC env , which can cause huge noise.

- Imagine you are part of fire brigade team and have centralized software where all the city's fire alarms are integrated.
- suppose you get many fire notifications at once , all for different places.
- when you get into those loactions , your team finds out most of those were only triggered by exessive smoke from cooking.
- Eventually , all the efforts will be a waste of time and resources.

- in a SOC with security solutions in place without human intervention,
- you'll end up focusing on more irrelevant issues.
- There are always the People who help the security soultion to identify truly harmful activities and enable a prompt response.

- The __People__ are known as the SOC team.
- This team has the following roles and responsibilities.

- __SOC Analyst (Level 1) :__
  - Anything detected by the security solutino would pass through these analysts first.
  - These are the first responders to any dection.
  - SOC level 1 analysts perform basic alert triage to determine if a specific detection is harmful.
  - They also report these detections through proper channels.

- __SOC Analyst (Level 2) :__
  - While Level 1 does the first-level analysis , some detections may require deeper investigation.
  - Level 2 Analysts help them dive deeper into the investigations and correlate the data from multiple data source to perform a proper analysis.

- __SOC Analyst (Level 3) :__
  - Level 3 Analysts are experienced professionals who proactively look for any threat indicators and support in the incident response activities.
  - The critical severity detectino reported by Level 1 and Level 2 Analysts are often security incidents that need detailed responses, including containment, eradication , and resovery.
  - This is where Level 3 analysts' experience comes in handy
 
- __Security Engineer :__
  - All analysts work on security solutinos.
  - These solutions need deployment and configuration.
  - Security Engineers deploy and configure these security solutions to ensure their smooth operation
 
- __Detection Engineer :__
  - Security rules are the logic built behind security solutions to detect harmful activities.
  - Level 2 and 3 Analysts often create these rules , while the SOC team can sometimes also utilize the detection engineer role independently for this responsibility,
 
- __SOC Manager :__
  - The SOC Manager manages the processes the SOC team follows and provides support.
  - The SOC Manager also remains in contact with the orgaziation's CISO (Chief information Security Officer) to provide him with updates on the SOC team's Current security posture and efforts
 
  _NOte : The Role in the SOC team can increase or decrease depending on the size and criticality of the Organiztions._

### Process
- We dicussed the roles and responsiblities of different individuls working in the SOC team.
- Each role has its own Processes.

#### Alert Triage:
- The alert triage is the basis of the SOC team.
- The first response to any alert is to perform the triage.
- The triage is focused on analyzing the specific alert.
- This determinses the severity of the alert and helps use prioritize it.
- The alert triage is all about answerting the 5 Ws.
- What are these 5 Ws?
  - Who
  - What
  - why
  - where
  - when
- Following are some wuestions that need to be answered during the triage of an alert.
- __Alert:__ Malware detected on Host: GEORGE PC
- _What? :_
  - A malicious file was detected on one of the hosts inside the organization's network
- _When? :_
  - The file was detected at 13:20 on June 5 , 2025
- _where? :_
  - The file was detected in directory of the host: "GEORGE PC".
- _who? :_
  - The file was detected for the user George.
- _why? :_
  - After the investigation , it was found that the file was downloaded from a pirated software-selling website.
  - The investigation with the user revealed that they downloaded the file as they wanted to use a software for free
 
#### Reporting
- The detected harmful alerts need to be escalated to higher-level analysts for a timely response and resolution.
- these alerts are escalated as tickets and assigned to the relevant people.
- The resport should discuss all the 5 Ws along with a through analysis , and screenshots should be used as evidence of the activity

#### incident Response and Forensics
- the reported detections point to highly malicious activities that are critical.
- in these sceenarios , high-level teams intiate an incident response.
- This forensic activity aims to determine the incident's root cause by analyzing the artifacts from a system or network.

### Technology
- Having the right people and Processes in place would never  be enough without security solutions for dection and response.
