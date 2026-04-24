#include <stdio.h>

int main()
{
    int i, n, t;
    int bt[10], rem_bt[10], wt[10], tat[10];
    int time = 0;
    float awt = 0, atat = 0;

    printf("============================================\n");
    printf("Round Robin Scheduling Algorithm\n");
    printf("============================================\n");

    printf("Enter number of processes: ");
    scanf("%d", &n);

    // Input burst time
    for(i = 0; i < n; i++)
    {
        printf("Enter Burst Time for Process %d: ", i + 1);
        scanf("%d", &bt[i]);
        rem_bt[i] = bt[i];  // copy for processing
    }

    printf("Enter Time Quantum: ");
    scanf("%d", &t);

    // Round Robin Logic
    int done;
    do
    {
        done = 1;

        for(i = 0; i < n; i++)
        {
            if(rem_bt[i] > 0)
            {
                done = 0;

                if(rem_bt[i] > t)
                {
                    time += t;
                    rem_bt[i] -= t;
                }
                else
                {
                    time += rem_bt[i];
                    tat[i] = time;
                    rem_bt[i] = 0;
                }
            }
        }
    } while(!done);

    // Calculate WT and averages
    for(i = 0; i < n; i++)
    {
        wt[i] = tat[i] - bt[i];
        awt += wt[i];
        atat += tat[i];
    }

    // Output
    printf("\nPROCESS\tBT\tWT\tTAT\n");

    for(i = 0; i < n; i++)
    {
        printf("P%d\t%d\t%d\t%d\n", i + 1, bt[i], wt[i], tat[i]);
    }

    printf("\nAverage Waiting Time = %.2f", awt / n);
    printf("\nAverage Turnaround Time = %.2f\n", atat / n);

    return 0;
}