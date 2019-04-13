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