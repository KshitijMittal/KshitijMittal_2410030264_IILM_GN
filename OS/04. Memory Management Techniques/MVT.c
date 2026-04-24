#include <stdio.h>

int main()
{
    int ms, mp[10], i, temp, n = 0;
    char ch = 'y';

    printf("============================================\n");
    printf("Memory Management - Variable Partitioning (MVT)\n");
    printf("============================================\n");

    printf("Enter total memory (Bytes): ");
    scanf("%d", &ms);

    temp = ms;

    for(i = 0; ch == 'y'; i++, n++)
    {
        printf("\nEnter memory required for process %d: ", i + 1);
        scanf("%d", &mp[i]);

        if(mp[i] <= temp)
        {
            printf("Memory allocated for Process %d\n", i + 1);
            temp -= mp[i];
        }
        else
        {
            printf("Memory Full\n");
            break;
        }

        printf("Do you want to continue (y/n): ");
        scanf(" %c", &ch);
    }

    printf("\nTotal Memory = %d", ms);
    printf("\n\nPROCESS\tMEMORY ALLOCATED\n");

    for(i = 0; i < n; i++)
    {
        printf("%d\t%d\n", i + 1, mp[i]);
    }

    printf("\nTotal Allocated Memory = %d", ms - temp);
    printf("\nExternal Fragmentation = %d\n", temp);

    return 0;
}