# Writeup 2 - OSINT

Name: Harshil S Patel
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Harshil S Patel

## Assignment Writeup

### Part 1 (45 pts)


1.What is v0idcache's real name?

Elizabeth Moffet


2. Where does v0idcache work? What is the URL to their website?

Banking CEO at 1337 BANK
http://1337bank.money/about 

 I used IntelTechniques to do a username search where i can across her twitter. Found this by finding the twitter page and then saw the link for her job. That give me the link to her website and i could see that she was the CEO. 




3. List all personal information (including social media accounts, contacts, etc) you can find about v0idcache. For each, briefly detail how you discovered them.

Github - v0idcache
Twitter -v0idcache
Reddit : u/v0idcache
email - v0idcache@protonmail.com, v0idcache@aol.com ,v0idcache@gmail.com, v0idcache@hotmail.com, v0idcache@yahoo.com 


 -> Used  Inteltechniques to do a username search and that provided me alot of the emails. 


Address - Leeteinde 12 , Broek, Waterland, 1151 AK, NL.  

-> I used who is on 1337bank.money and that provided alot of information. 

Contact:
name:         Serina Ness
organisation: Donuts Inc.
address:      Donuts Inc.
address:      5808 Lake Washington Blvd NE, Suite 300
address:      Kirkland, WA 98033
address:      United States
phone:        +1.425.283.8248
fax-no:       +1.425.671.0020
e-mail:       serina@donuts.email

-> I used who is on 1337bank.money and that provided this information. 





4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.

ipaddress -142.93.136.81 -> Netherlands
DNS Servers : 216.87.155.33
DNS Servers : 216.87.152.33
MX Records : 162.255.118.61. 


MX Records : 162.255.118.61

-> To find this information i used the tools that we learned in class the main one i used was DNSDumpster.com. 
This also provided me with a flag.


5. List any hidden files or directories you found on this website. For full credit, list two distinct flags.
secret_directory



CMSC389R-{h1dd3n_1n_plain_5ight} -> I inspected the HTML code of the website and i found this flag in there as a comment.

CMSC389R-{h1ding_fil3s_in_r0bots_L0L}  -> I found this by using /robots.txt on the website which told me what directory was there. From there I was able to navigate to the directory and get the Flag. 


6. What ports are open on the website? What services are running behind these ports? How did you discover this?

22- SSH
80 -HTTP
1337 - waste

I used nmap to run a search on targeted ports from 100 - 2000. This returned the open ports as 22, 80 and 1337. Funny as the answer was in the link the whole time. 

7. Which operating system is running on the server that is hosting the website? How did you discover this?

UBUNTU

I used https://censys.io to find that information.

8. 



CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}

CMSC389R-{brut3_f0rce_m4ster}

CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}

CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}

CMSC389R-{2bmPrIPj1k13iMrKYS5e4vkZI}








### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!*

At first i wasn't sure on how to do this. I had to go online and look at the socket libary and see how it worked. Once i understood how it worked it was just a matter of running a for loop for every single password in the rockyou wordlist. A couple times i thought i was doing it wrong because the server was down and i wasn't getting a response. After a bit a debugging and once the server was back online I was able to get the password as "linkinpark". After getting into the system i tried searching for the file AB4300.txt that i found from the pastebin. I wasn't getting any hits for that so then i started manually going into all the folders and looking for the file until i went into the home folder and saw the flag.txt file which i found another flag in. Then i went in the files folder and saw all the txt files so i did cat AB4300.txt and i was able to open it and get the last flag. 


To run the file just do python3 hack.py and that should run it. Although it only worked for me on Kali and iout wasn't working on my Mac. If you need to update the file location in the file you can aswell. 
