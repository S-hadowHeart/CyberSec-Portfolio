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
   
2.Consider a class B network with 180-subnets and 200 host
