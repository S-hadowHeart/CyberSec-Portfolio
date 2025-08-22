# Classful Addressing

## Class A 
- 1 bit fix `0` (First bit)
- Total ip : 2^31
- Network id: 08 bit
- Host id: 24 bit
- Range: 1 - 126
- Total Number of network : 2^7 - 2 = 126
- Total Number of host : 2^24 -2
   - __127 . x . x . x can't be used as a source IP(SIP)(total add 2^24)__
   - __it always be used as a destination IP Address (DTP)__
   - __it  reserved for some special purpose so at can't be assigged to any computer (Host)__
   - __127.0.0.0 and 127.255.255.255 not will use (we will discuss in future why)__
     
## Class B :
 - 2 bit fix `10` (First two bit)
 - Total ip : 2^30
 - Network id: 16 bit
 - Host id:    16 bit
   
                   Let's Find Range of ip
                   __10__ 000000 . x . x . x  -->  128
                   __10__ 000001 . x . x . x  -->  129
                   __10__ 000010 . x . x . x  -->  130
                         .
                         .
                         .
                         .
                         .
                   __10__ 111111 . x . x . x  -->  191
   - Range : 128 to 191
   - no possibility of all 0 or 1 so no need to remove any netowork ^^) 
   - Total number of network: 2^14
   - Total number of host:    2^16 __but but__ in host all can be x.x.0.0 and x.x.255.255 so we can't assign any computer
   
   
                   so really __2^16 -2__
   
## Class C :
- 3 bit fix `110` (First three bit)
- Total ip   : 2^29
- Network id : 24 bit
- Host id    : 08 bit
- Range : 192 to 223
- Total number of network : 2^24 but removing fix bit(First 110)

                 so really __2^21__
- Total number of Host    : 2^8 but removing 0 and 1(255)

                so really __2^8 -2__

## Class D :
- 4 bit fix `1110`(First 4 bit)
- Total ip : 2^28
- Network id : ???
- Host id : ???
  - __No Network id and No Host id in class D__
  - __Class D is Reserved For Multicasting__
- Range : 224 to 239

## Class E :
- 4 bit fix `1111` (First 4 bit)
- Total ip : 2^28
  - __No network id and No Host id in Class E__
  - __Class E is Reserved for research and Future Purpose__
- Range : 240 to 255 (here last network is all 1 but rule was if host/network id is 0 or 1 then cancel that we don't have here 🫠)
