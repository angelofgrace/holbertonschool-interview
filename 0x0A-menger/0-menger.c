#include "menger.h"

/**
 * menger - Draws a 2D menger sponge
 * 
 * @level: the level of the monger sponge to draw
 * 
 * Return: void (output)
 */
 void menger(int level)
 {
    int i, j, dhi, dwid;

    if (!level || level < 0)
    {
        return;
    }
    else if (level == 0)
    {
        printf("#");
    }
    for (i = 0; i < pow(3, level); i++)
    {
        for (j=0; j < pow(3, level); j++)
        {
            dhi = i;
            dwid = j;
            while(1)
            {
                if (dhi % 3 == 1 && dwid % 3 == 1)
                {
                     printf(" ");
                     break;
                }
                else if (dhi == 0 || dwid == 0)
                {
                    printf("#");
                    break;
                }
                dhi /= 3;
                dwid /= 3;
            }
        }
        printf("\n");
    }
 }
