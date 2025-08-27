# Introduction to subneting
## Classful Addressing:
- Class A -> 2^24 IP addresses int one nework
- Class B -> 2^16 IP address in one netwokr
- Class C -> 2&8 IP address in one network


# Subnetting:
- The process of dividing a big network to many smaller subnet is called as subnetting.
- __Advantage:__
  - Maintenance and Administration is simple and easy
  - it provides security to one Network from another Network
  - Example:
    - Code of developer department must not be accessed by another department
- __DisAdvantage:__
  1. Subnettting complicates the communication process.
  - Instead of 3 step pocedure now it becomes 4 step procedure
    - __Step 1:__
      - Identify the Network
    - __Step 2:__ 
      - Identify the Subnet with in the Network
    - __Step 3:__
      - IDentify the host with in the Subnet
    - __Step 4:__
      - Identify the process with in the Host.
  2. In case of single Network only two IP addresses are wasted to represent Network and direct Broadcast Address but in case of subnetting two Ip address are wasted for each subnet
  3. Cost overall Network also increase.
    - Subnetetting reuires internal routers , Switches , Hub , bridges etc. which are very costly.
  4. Subnetting and Network management require an experienced network administrators This adds to the overall cost as well.
__Note:__
- The Process of Borrowing bits from HID to generate the subnet ID is also called as subnetting
- Number of bit Borrowed depends on our Reuirement.
