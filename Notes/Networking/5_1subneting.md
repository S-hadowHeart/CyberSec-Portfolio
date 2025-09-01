# Subnetting Category 1
 - finding network and broadcast address 
   - just all 0 after subnetthing in host id then it will network subnet id (__SID__)
   - all 1 after subnetthing in host id then it will Direct broadcast address (__DBA__)
  
### How to find totol ip after subnetting:
- example net id is `8` and you want to divide this into 8 parts , write now total ip is `2^8`
- To find total ip in per subnet `2^8(totol ip in network)/ 8 (parts/subnet)` = `2^8/2^3` = `2^(8-3)` = `2^5` total ip in per subnet
  
NOte: 
- full network id and 1st SID will same
- last subnet DBA and and last ip of netowrk will same
- so what they actually they represent ?
   
