# Writeup 3 - Operational Security and Social Engineering

Name: Harshil S Patel	
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Harshil S Patel
## Assignment Writeup

### Part 1 (40 pts)




You have been hired by a penetration testing firm and have been asked to collect some specific information about the 1337Bank employee from HW2, Elizabeth Moffet. Some of the information you're looking for seems to be unavailable or unlikely to be found through OSINT:

Many of the questions that are being asked are common security question for many different accounts. From our knowledge of OSINT we are able to find out where she has accounts and from there we can target some of these questions by giving the customer service center for these accounts a call and figuring out which accounts have some of these questions. The quesiton where they say what is her mother maiden name is a very common security question and you might find that with ease by calling 1 or 2 companies. For the question that is asking what browser does she primarily use you can pretend that you are calling from her internet service provider and say that someone has been accessing unlawful or illegal content from her ip address. From there we can go through some trouble shooting to "try" and help her get a more secure wifi connection and we can ask her what broswer she is using and suggest that she use any other browser for "security reasons". The question for what city she was born in while we are talking to her about her internet we can throw in some random chit chat like what do you do for a living since we know she is a CEO at a bank and then from there we can pretend surprised and say you have a friend from the city where the bank is located and you can throw in were you born and raised there aswell? For the ATM pin number it would be kind of tough but with the right OSINT information and after gettting some information like her mother's maiden name and what city she was born in, we can pretend to be calling from her bank and then ask her to verify her identity with those 2 security question. Once she "successfully" verifies her identity we can tell her that we had blocked her card for some suspiscous activity on her account and that we have to send her a new ATM but before we can send her a new one we have to unlock her card with her ATM pin number. For the last question we have to get kind of creative, so we can pretend to be calling from a local animal shelter where she grew up and then ask about some infromation about her past and current pets for a survey that they are running. 



### Part 2 (60 pts)

Running a WhoIs on Elizabeth Moffets domain gave us all the information about her and her contact. This stuff can be dangerous espceially when you are running a organization because it leaves you vunerable to attacks like the one fron 389r. For organzations such as her bank they should either invest in a private domain so that they can disgusie their identity and not have all their infomation public. Having a private domain would give you more security from the public as we were able to get all her infromation with a simple whois. 

http://www.networksolutions.com/education/you-need-private-registration/

Running nmap on 1337bank.money exposed that there was an open port and it gives you what service is running on that port. Attackers can use this information to do a number of harmful things such as; buffer overflow or any other remotely exploitable attack. 
https://www.acunetix.com/blog/articles/danger-open-ports-trojan-trojan/

One last thing that i would recommend is that she choose better passwords. Her password was able to be guessed with a brute force method and a wordlist. If your password can be guesseed through a wordlist then that password is not a good password. I would suggest that she use a password strength checker in order to check the strength of her password so that she can she how strong her password is. 

http://www.passwordmeter.com/
