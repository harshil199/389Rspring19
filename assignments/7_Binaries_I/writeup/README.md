# Writeup 7 - Binaries I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (90 Pts)

#include <stdio.h>

int main()
{
// Assign values to a and b
int str1 = 0x1ceb00da;
int str2 = 0xfeedface;

// Print the value of a
printf("str2 = %d\n", str2);

// Print the value of b
printf("str1 = %d\n", str1);

// Swap the values of a and b
str2 ^= str1;
str1 ^= str2;
str2 ^= str1;

// Print the value of a
printf("str2 = %d\n", str2);

// Print the value of b
printf("str1 = %d\n", str1);

return 0;
}


### Part 2 (10 Pts)

The program prints the 2 values from addresses and then takes 2 values from memory and performs an XOR on them 3 times. After doing that it prints the value. 



