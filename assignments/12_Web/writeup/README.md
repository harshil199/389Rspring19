# Crypto II Writeup

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (40 Pts)

Looking around for the question for part 1 i was kind of confused so i resorted to piazza and thats when i realized that the title spelled SQL. So when i went to the website and i clicked on the different links i saw IRL id = {}. So then i tried to use SQL injection to get the flag and i saw that when i tried 1=1 i got a sql injection detected error. So i tried a lot of different combination but the one that ended up working for me was http://1337bank.money:5000/item?id=1' || '1'='1 thats how i got the flag CMSC389R-{y0u_ar3_th3_SQ1_ninj@}


### Part 2 (60 Pts)

Level 1: 

I put <script>alert();</script>, i know a little javascript so i know thats how you execute an alert. 

Level 2: 

This one was much more harder because it took me alot of guessing and i still couldn't figure it out so then i had to look at the hints. The last hint helped me out because i was able to get it to work with the onerror attribute. So i inserted this  <img src = "image.jpg" onerror = alert("Hello")> and i was able to advnace to the next level. It doesn't find a valid path so it executes the alert. 

Level 3:
I had to look at the source code for this and thats when i saw that the buttons are invoking the function choosetab. The function takes the values that were in the url and it doesn't filter them and just adds them to the html. So thats when i realized that we can use this to inject code in the url. SO then i added the same thing from the last level and put  ' onerror="alert('done');" and that let me advnace to the next level. 

level 4: 
I saw that this level actually had a entry box so i figured we would have to do something with it. I couldn't figure out exactly what to do so i looked at the hints and and the third hint helped. I figured out i needed to put the injection in where the number of seconds had to go. So i played around with the alert for a while and i couldn't get it to work so i looked at timer.html and saw line 21 where the code was going so i figured the best way to inject would be alert(‘xss, hello. ');alert('xss.

level 5: 

when i clicked the signup button i saw the the utl changed to signup?next=confirm so i figured that we have to replace next with with something so i tried a few comibination and the only one that seemed to work was when i put this in the url and in the signup box ?next=javascript:alert('hello'). 

Level 6: 
This was the hardest level for me because i was really confused for a while, so i decided to go and look at the hints so then and i saw that one of them said to use a online api. So then i used the suggested api and and did https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert and that worked. 