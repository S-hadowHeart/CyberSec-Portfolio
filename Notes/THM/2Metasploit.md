# Metasploit
- is open source penetration testing framework that helps security professionals find and exploit vulnerability in computer system
- it includes a database of known vulnerabilities and tools and scripts for exploiting them.
## __Two Main Versions__
  - Metasploit Pro:
    - The commercial version that facilitates the automation and management of tasks.
    - This version has a Graphical user interface (GUI).
  - Metasploit Frameworks:
    - The open-Source version that works from command line.

- __Metasploit Framework is set of tools allow information gathering,scanning,exploitation,exploit development,post-exploitaion,and more.__
- __while the primary usage focuses on penetration testing domain,it's also use for vulnerbillity research and exploit development__

### Main Components
  - msfconsole: The Main Command line interface.
  - Modules : supporting modules such as exploits, scanners, payloads, etc.
  - Tools :
    - Stand-alone tools that will help vulnerability research,vulnerbility assessment(scanning of a system or network for known vulnerbilities), or penetration testing.
    - some of this tools are msfvenom,pattern_create and pattern_offset.
    - pattern_create and pattern_offset are tools useful in exploit development.

### type __msfconsole__ to start
  - console will your main interface to interact with the different modules of the Metasploit Framework.
     - modules are small components within the metasploit framework that are buit to perform a specific task
        - such as exploting a vulnerability,scanning a target or performing a brute-force attack

  - __Exploit__ :
    - A piece of code that uses vulnerability present on the target system.
  - __vulnerability__ :
    - A design,coding ,or logic flaw affecting the target system.
    - The exploitation of vulnerability can result in disclosing confidential information or allowing the attacker to execute code on the target system. 
  - __payload__:
    - An exploit will take advantage of a vulnerabilty.
    - however,if we want the exploit to have the result we want(gaining access , read confidential info , etc),we need to use payload.
    - payloads are the code that will run on the target system.
      
- Auxiliary :
  - Any supporting module , such as scanners , carawlers and fuzzers, can be found here.
- Encoders :
  - Encoders will allow you to encode the exploit and payload in the hope that a signature-based antivirus solution may miss them.
  - __signature-based antivirus and security solutions__ :
  - have a database of known threats.
  - They detect threats by comparing suspicious files to this database and raise an alert if there is a match
  - Thus encoders can have a limited success rate as antivirsus solutions can perform additional checks.

-  Evasion :
  - While encoders will encode the payload, they should not be considerd a direct attempt to evade antivirus software.
  - on the other hand , "evasion" modules will try that , with more or less success

- Exploits :
  - Exploits , neatly organized by target system.

- NOPs :
  - NOps (No OPeration) do nothing, literally.
  - They are represented in the intel x86 CPU family with 0x90,
  - following which the CPU will do nothing for one cycle.
  - They are often used as a buffer to achieve consistent payload sizes

- Payloads:
  - Payloads are codes that will run on the target system.
  - Exploits will leverage a vulnerability on the target system,
  - but to achieve the desired result , we will need a payload.
  - Examples could be:
    - getting a shell , loading a malware or backdoor to the target system, running a command , or launching calc.exe as a proof of concept to add to the penetration test report.
    - starting the calulator on the target system remotely by launching the calc.exe application is a benign way to show that we can run commands on the target system.
  
  - Metasploit offers the ability to send diffrent payloads that can open shells on the target system for interactive connection.
  - Four different directories under payloads:
      - __Adapters:__
        
        - wraps single payloads to convert them into diffrent formats.
        - Example:
            - A normal single payload can be wrapped inside powershell adapter, which will make a single powershell command that will execute the payload
              
      - __Singles:__
        - self-contained payloads(add user, launch notepad.exe etc)
        - that do not need to download an additional component to run
    
      - __Stagers__ :
        - Responsible for setting up connection channel between Metasploit and the target system.
        - useful when working with staged payloads
        - _Staged payloads_ :
          - First upload a stager on the target system then download the rest of the payload(stage).
          - This provides some advantages as the intial size of payload will be relatively small compared to the full payload sent at once
      - __Stages__ :
        - Downloaded by the stager.
        - This will alllow you to use larger sized payloads.

### __inline payloads__
  - Metasploit has a subtle way to help you identify single(also called "inline") payloads and staged payloads
    - generic/shell_reverse_tcp
    - windows/x64/shell/reverse_tcp
  - bothe are reverse windows shells
  - indicated by the "_" between "shell" and reverse
  - while the latter is staged payload, as indicated by the "/" between "shell" and "reverse".

### __Post__ :
  - post modules will be useful on the final stage of penetration(post-exploitation).
 

## Let's move to Practical:
 - using msfconsole we can start metasploit that everyone know
 - you can still use command like ls,ping etc normally
 - but still some command not support (e.g output redirection, help> help.txt)
 - whenever you change between module you need to reset __RHOSTS__ again

 - use exploit/windows/smb/ms17_010_eternalblue command:
   - command line prompt change from msf6 to "msf6 _exploit(windows/smb/ms17_010_eternalblue)
   - module to be used can also be selected with `use` command
     - followed by number at the beginning of the search result line
   - __EternalBlue:__
     - Developed by Us National security Agency(NSA)
     - For a vulnerability affecting the SMBv1 server on numerous windows systems.
     - The SMB(server Message Block) is widely used in windows networks for file sharing and even for sending files to printers.
     - EternalBlue was leaked by the cybercriminal group "shadow Brokers" in Aprill 2017.
     - in May 2017, the vulnerbility was exploited worldwide in the WannaCry ransomeware attack


## Basic Commands:

- __`show options`:__
 - this will print options realted to the exploit we have chosen earlier.
 - have different outputs depending on the context it is used in.
 - Ex for above require set variables like RHOSTS and RPORT

- __`show`__ :
  - show command can be used in any context followed by module type(auxiliary,payload, exploit etc, ex: `show payloads`)
 
- __`back`__ :
  - leave the context (ex: back from exploit to main console)

- __`info`__ :
  - Further info on any module can be obtained by typing info within its context
  - alternative to use :
    - `info exploit/windows/smb/ms17_010_eternalblue`
    - it's not help menu
    - it will display detailed info on the module such as its author,relevant sources, etc

- __`search`__:
  - This command will search the Metasploit Framework database for modules relevant rto given search parameter.
  - you can conduct searches using CVE numbers, exploit names(eternalblue,heartbleed,etc) or target system.
  - it's provides an overview of each returned module
  - Example for if you want search results to only include auxilliary modules
    - `search type:auxiliary telnet`

- To set any parameter:
  - `set  `PARAMETER_NAME VALUE`
 
- __Parameters you will often use are:__
  - RHOSTS:
    - "Remote host"
    - ip of target system
    - A single ip address or a network range can be set
    - This will support the CIDR(Classless inter-Domain Routing) notation (/24,/16, etc) or a network range (10.10.10.x - 10.10.10.y)
    - u can also use a file where targets are listed
      - one target per line using file: /path/target_file.txt

  - RPORT:
    - "Remote port"
    - port on the target system the vulnerable application is running on

  - PAYLOAD:
    - The Payload you will use with the exploit

  - LHOST: 
    - "Localhost"
    - the attacking machine ip address

  - LPORT:
    - "Local port"
    - port you will use for the reverse shell to connect back to.
    - port on attacking machince and you can set it to any port not used by any other application.

  - SESSION :
    - Each connection established to the target sytem using Metasploit will have a session ID.
    - you will use this with post-exploitation modules that will connect to the target system using an existing connection

  - __`unset` to clear any parameter value or `unset all` for all__

  - __`setg` use to set parameter default across diffrent modules. you can clear any value `unsetg` that set with `setg`__

  - `exploit` or `run`(alias for exploit):
    - use to launch module
    - can you without any parameters
    - or using `-z` parameter
      - `exploit -z` run exploit and background the session as soon as it opens.
    - will return context prompt from which you have run the exploit
    - some modules support the `check` option
      - This will check if the target system is vulnerable without exploiting it

  - Sessions:
    - Once a vulnerblity has been successfully exploited,a session will be created.
    - This is the communication channel established between the target system and Metasploit
    - you can use `background` command
      - to background session prompt and go back to the msfconsole prompt
      - alternatively just press `ctrl+z` to background sessions
    - `sessions` use in any context to see the existing sessions.
      - to interact with any session, use `sessions -i` fommand followed by desired session number
      - example `sessions -i 1`
      -     
