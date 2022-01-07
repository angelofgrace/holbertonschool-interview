#include "palindrome.h"


/**
 * is_palindrome - checks if an unsigned long int is a palindrome,
 * notably, tasked with not allocating addl memory, otherwise
 * a recursive version would be more efficient in terms of time complexity
 * @n: ulong to evaluate
 * Return: 1 if palindrome, else 0
**/
int is_palindrome(unsigned long n)
{
    /* int var for last digit, building a reverse version, */
    /* and a manipulable copy of input */
    int lastDig = 0;
    unsigned long int tempN = n, reverse = 0;

    tempN = n;

    /* while depleting value is greater than 0 */
    while (tempN)
    {
        /* isolate last digit */
        lastDig = tempN % 10;
        /* append last digit to build reverse of input */
        reverse = (reverse * 10) + lastDig;
        /* deplete temporary var */
        tempN = tempN / 10;
    }
    
    return (reverse == n);
}