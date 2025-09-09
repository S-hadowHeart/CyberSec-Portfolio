## Introduction
- CyberChef is a simple , intuitive web-based application designed to help with various "cyber" operation tasks within your web browser.
- __Two methods to access cyberchef__
  - __Online Access :__
    - All you need is web browser and internet connection.
    - Then you can click this https://gchq.github.io/CyberChef to open cyberchef directly within your web browser.
  - __Offline or Local Copy :__
    - you can run this offline or locally on your machine by downloading the latest release file from this https://github.com/gchq/CyberChef/releases
    - This will work on both Windows and Linux platforms.
    - As best practice , you should download the most stable version.
   
## Navigating the interface
- Cyberchef considts of four areas, Each consists of different components or features
- These are the following areas:
  1. Operations
  2. Recipe
  3. Input
  4. Output

     <img width="2984" height="1660" alt="image" src="https://github.com/user-attachments/assets/52c7c471-77e8-4b16-97a5-78537debe87a" />

### The Operations Area:
- __From Morse Code :__
  - Translates Morse code into (upper case) alphanumeric chracters.
  - Example:
    - `- .... .-. . .- - ...` becomes `THREATS` when used with default parameters
- __URL Encode :__
  - Encodes problematic chracters into percent encoding , a format supported by URIs/URLs
  - Example:
    - `https://google.com` becomes `https%3A%2F%2Fgoogle%2Ecom` when used with parameter "Encode all special chars"
- __To Base64 :__
  - This operation encodes raw data into an ASCII Base64 string.
  - Example :
    - `This is fun!` becomes `VGhpcyBpcyBmdW4h`
- __To Hex :__
  - Converts the input string to hexadecimal bytes separated by delimiter.
  - Example:
    - `This Hex conversion is awesome!` becomes `54 68 69 73 20 48 65 78 20 63 6f 6e 76 65 72 73 69 6f 6e 20 69 73 20 61 77 65 73 6f 6d 65 21`
- __To Decimal :__
  - Converts the input data to an ordinal integer array.
  - Example :
    - `This Decimal conversion is awesome!` becomes `84 104 105 115 32 68 101 99 105 109 97 108 32 99 111 110 118 101 114 115 105 111 110 32 105 115 32 97 119 101 115 111 109 101 33`
- __ROT13 :__
  - A simple Caesar subsitution cipher which rotates alphabet characters by the specified amont (default 13)
  - Example:
    - `Digital Forensics and Incident Response` becomes `Qvtvgny Sberafvpf naq Vapvqrag Erfcbafr`
_Alternatively , you can directly check how the operations work by hovering on the specific operation. This should give you a sample or a description and link to wiipedia._

### The Recipe Area:
- This considered as  the heart of the tool. in this area ,
- you can seamlessly select,arrange , and fie-tune operations to suit your needs.
- __Feature include the following:__
  - `Save recipe` : This feature allows the user to save selected operations.
  - `Load recipe` : Allows the user to load previously saved recipes.
  - `Clear Recipe` : This feature will enable users to clear the chosen recipe during usage.
  - bottom `BAKE!` button. This porcesses the data with the given recipe
  - you can tick the `Auto Bake` checkbox : this feature allows users to automatically cook using the selected recipe without manually clicking `BAKE!` every time. 
