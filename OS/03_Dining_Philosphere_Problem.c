#include <stdio.h>
#include <stdlib.h>

int tph, philname[20], status[20], howhung, hu[20], cho;

void one();
void two();

int main()
{
    int i;

    printf("============================================\n");
    printf("Dining Philosopher Problem\n");
    printf("============================================\n");

    printf("\nEnter the total number of philosophers: ");
    scanf("%d", &tph);

    for(i = 0; i < tph; i++)
    {
        philname[i] = i + 1;
        status[i] = 1;
    }

    printf("Enter number of hungry philosophers: ");
    scanf("%d", &howhung);

    if(howhung == tph)
    {
        printf("\nAll philosophers are hungry...");
        printf("\nDeadlock may occur!");
        printf("\nExiting...\n");
        return 0;
    }

    for(i = 0; i < howhung; i++)
    {
        printf("Enter philosopher %d position: ", i + 1);
        scanf("%d", &hu[i]);
    }

    do
    {
        printf("\n\n1. One can eat at a time");
        printf("\n2. Two can eat at a time");
        printf("\n3. Exit");
        printf("\nEnter your choice: ");
        scanf("%d", &cho);

        switch(cho)
        {
            case 1: one(); break;
            case 2: two(); break;
            case 3: exit(0);
            default: printf("\nInvalid option...");
        }
    } while(1);

    return 0;
}

void one()
{
    int i, j;

    printf("\n\n--- Only One Philosopher Eats at a Time ---\n");

    for(i = 0; i < howhung; i++)
    {
        printf("\nP%d is eating", philname[hu[i]]);

        printf("\nOthers waiting: ");
        for(j = 0; j < howhung; j++)
        {
            if(j != i)
                printf("P%d ", philname[hu[j]]);
        }
        printf("\n");
    }
}

void two()
{
    int i, j, count = 0, k;

    printf("\n\n--- Two Philosophers Can Eat Simultaneously ---\n");

    for(i = 0; i < howhung; i++)
    {
        for(j = i + 1; j < howhung; j++)
        {
            if(abs(hu[i] - hu[j]) != 1 && abs(hu[i] - hu[j]) != tph - 1)
            {
                count++;
                printf("\nCombination %d:", count);
                printf("\nP%d and P%d are eating", philname[hu[i]], philname[hu[j]]);

                printf("\nOthers waiting: ");
                for(k = 0; k < howhung; k++)
                {
                    if(k != i && k != j)
                        printf("P%d ", philname[hu[k]]);
                }
                printf("\n");
            }
        }
    }

    if(count == 0)
    {
        printf("\nNo valid combinations possible (avoiding deadlock)\n");
    }
}