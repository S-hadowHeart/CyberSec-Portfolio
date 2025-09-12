## Category  2

1. Consider a Class C network with 7-subnets and 25 hosts per subnet.An appropriate subnet Mask for this network?
Ans. - First check if possible:
     7 * 25 = <= 2^8 -2
     175 = 254 (yes possible)
   - class c Network id - 24 bit , host id - 8 bit
   - for 7 subnet we need 3 bit so , take borrow , hid now 5
   -  2^3 - 8 subnet , 2^5 -2 = 30 host/subnet
   -  so now , NID = 24 , SID = 3 , HID = 5
   -  _NO. if 1's in the s.m = NID + SID = 24 + 3  =27_
   -  _NO. of 0's in the S.m = HID=5
   -  subnet mask = 255.255.255.224 (best)
   -  but you can take any 1 so , it can be also = 255.255.255.7 or this also possible 255.255.255.44 etc (we can any where 1's) (so any subnet mask where 27 `1` that will possible)
   -  
   
2.Consider a class B network with 180-subnets and 200 hosts per subnet. An appropriate subnet Mask for this network?
Ans 
 - First check if possible:
   - Class-B
   - 180 *200 <= 2^16 -2
   - 360000 <= 65534 (yes)

- Class B (NID 16b and HID 16b)
  - we nee to make 180 subnet
  - so using 7b we can make only 127 so we need 8b
  - so SID - 8b , HID -  8b
  - No of Host|subnet = 2^8 -2 = 254
  - N of Subnet = 2^8 = 256

- Now let's find Subnetmask
- BEst :
- No of 1's in the s.m = NID + SID = 16 + 8 = 24
- No of 0's in the s.m = HID = 8
- 255.255.255.255.0 (Best)
- but other can possible that we dicuss before ..

3.Consider a Class C network with 15-subnets and 20 hosts per subnet.An appropriate Subnet Mask for this network ?
Ans
- First check if possible :
- Class-cc
- 15*20 <= 2^8 -2
- 300 <= 254 (No , not Possible)
why ?
 - Class c (NID = 24 , HID - 8 )
 - We need 15 subnet
 - if we take 4b of SID then remain HID is 4b
 - so 2^4 = total 16 subnet can we create
 - each subnet can have 2^4-2 = 14 host per subnet
 - that is not full fill our requirement cuz we want 20 host in per subnet , so (__Not possible__)

4. Consider a Class C network with 3-subnets and 60,60,120 hosts per subnet, An appropriate subnet Mask for this network?
Ans:
 - Example :
    - CE A = 120 student
    - CE B = 60 student
    - CE c = 60 student
      - toatal 240 = 2^8 -2 (yes possible)
     
 - __Case 1:__
 - Class - C  (NID 24b , HID 8b)
 - 3 subnet we need
 - so 2b SID , 6b HID
 - toatl subnet 2^2 = 4 subnet
 - 2^5 - 2 = 62 host per network
 - sp CEA students need not full fill

 - __Case 2 :__
 - NID 24 , HID 8
 - 1 SID , 7 HID
 - 2^1 = 2 subnet
 - 2^7-2 = 126 host per subnet
 - here CEA need full fill but CEB and CEC can't

_Note: Both the case are possible here TO solve this problem we use __VLSM__ technique._


## SUBNETTING CATEGORY 4 _VLSM_
1. Consider a Class C network with 3 subnets and 60,60,120 hosts per subnet.
- An appropriate Subnet Mask for this network ?
ANS :
 - Example:
 - CE A = 120
 - CE B = 60
 - CE C = 60
 - Total = 240 hosts

 - Class C (NID 24b , HID 8b)
 - if we take SID 1b then HID will 7b
 - Toatal subnet 2^1 = 2 subnet
 - host per subnet here - 2^7 -2 = 126 host per subnet
 - now 1 part we can give to CSEA ,
 - now our remain HID 7b we divide again
 - 1b SID so 6b HID
 - toatol subnet 2^1 = 2 ,
 - Total host per subnet 2^6 -2 = 62 host per subnet
 - so now we can give this two subnet to CEB and CEC 

      
3. Consider a Class network with 3-subnets and 130,50,50 hosts per subnet. An appropriate subnet Mask for this network ?
- This will not possible. . even you try VLSM
