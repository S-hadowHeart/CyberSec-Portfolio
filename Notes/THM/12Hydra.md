# Hydra
- Hydra is a brute force online password caracking program
- a quick system login password "hacking" tool
- can run through a list and "brute force" some authentication services.
- A one-hundered-million-password list contains common passwords , so when an out of the box application uses an easy password to login ,

## installing Hydra
- pre-installed in kali linux
- for ubuntu or fedora system
- `apt install hydra` or `dnf install hydra`.


## Hydra Commands
- The options we pass into Hydra depend on which service(protocol) we're attacking
- __Example:__
  - if we wanted to brute force FTP with the username being `user` and password list being `passlist.txt`
  - we do use the following command:
  - `hydra -l user -P passlist.txt ftp://Machine_ip`
- __SSH:__
   - Command : `hydra -l <username> -P <full path to pass> MACHINE_IP -t 4 ssh`
     - **`-l`** : specifies the(SSH) username for login
     - **`-P`** : indicates a list of passwords
     - **`-t`** : sets the number of threads to spawn
     - Example:
       - `hydra -l root -P passwords.txt 192.168.12.12 -t 4 ssh`
         - Hydra will use root as the username for `ssh`
         - it will try the passwords in the `passwords.txt` file
         - There will be four threads running in parallel as indicated by `-t 4`
- __Post Web Form__
  - we can use Hydra to brute force web forms too
  - you must know which type of request it is making; GET or POST methods are commonly used.
  - you can use your browser's network tab (in developer tools) to see the request typesor view the source code
  - `sudo hydra <username> <wordlist> MACHINE_IP http-post-form  "<path> :<login_credentials>:<invalid_response>"`
    - **`-l`** : the username for (web form) login
    - **`-P`** : the password list to use
    - **`http-post-form`** : the type of the form is POST
    - **`<path>`** : the login page URL. for example, `login.php`
    - **<login_credentials>** : the username and password used to log in, for example `username=^USER^&password=^PASS^`
    - **`<invalid_response>`** : part of the response when the login fails
    - **`-V`** : verbose output for every attempt
  - __Example__ for brute force as POST login form:
  - `hydra -l <username> -P <wordlist> MACHINE_IP http-post-form "/:username=^USER^&password=^PASS^:F=incorrect" -V`
    - The login page is only `/` , i.e., the main IP address
    - THe `username` is the form field where the username is entered
    - The specified username(s) will replace `^USER`
    - The `password` is the form field where the password is entered
    - The provided passwords will be replacing `^PASS^`
    - Finally, `F=incorrect` is a string that appears in the server reply when the login fails
