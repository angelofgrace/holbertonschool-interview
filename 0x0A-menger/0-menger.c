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
    int i;

    if (!level || level < 0)
    {
        return;
    }
    if (level == 0)
    {
        printf("#");
        return;
    }
    for (i = 0, i <= level*3, i++)
    {
        writeMenger(level);
        return(menger(level - 1));
    }
 }

void writeMenger(level)
{
    int i, j;

    while (j >= level)
    {
        for (i = 0, i < 9, i++)
            if (i != 5)
            {
                printf("$");
            }
        j--
    }
}