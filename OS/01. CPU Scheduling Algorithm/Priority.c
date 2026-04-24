#include <stdio.h>

int main()
{
    int p[20], bt[20], pri[20], wt[20], tat[20];
    int i, j, n, temp;
    float wtavg = 0, tatavg = 0;

    printf("============================================\n");
    printf("Priority Scheduling Algorithm\n");
    printf("============================================\n");

    printf("Enter number of processes: ");
    scanf("%d", &n);

    // Input
    for(i = 0; i < n; i++)
    {
        p[i] = i + 1;  // P1, P2...
        printf("Enter Burst Time and Priority for Process %d: ", i + 1);
        scanf("%d %d", &bt[i], &pri[i]);
    }

    // Sorting based on priority (lower value = higher priority)
    for(i = 0; i < n - 1; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            if(pri[i] > pri[j])
            {
                // swap priority
                temp = pri[i];
                pri[i] = pri[j];
                pri[j] = temp;

                // swap burst time
                temp = bt[i];
                bt[i] = bt[j];
                bt[j] = temp;

                // swap process id
                temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
        }
    }

    // First process
    wt[0] = 0;
    tat[0] = bt[0];

    // Calculate WT and TAT
    for(i = 1; i < n; i++)
    {
        wt[i] = wt[i-1] + bt[i-1];
        tat[i] = tat[i-1] + bt[i];
    }

    // Averages
    for(i = 0; i < n; i++)
    {
        wtavg += wt[i];
        tatavg += tat[i];
    }

    // Output
    printf("\nPROCESS\tPRIORITY\tBT\tWT\tTAT\n");

    for(i = 0; i < n; i++)
    {
        printf("P%d\t%d\t\t%d\t%d\t%d\n",
               p[i], pri[i], bt[i], wt[i], tat[i]);
    }

    printf("\nAverage Waiting Time = %.2f", wtavg / n);
    printf("\nAverage Turnaround Time = %.2f\n", tatavg / n);

    return 0;
}