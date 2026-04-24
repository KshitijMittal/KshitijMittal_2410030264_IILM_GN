#include <stdio.h>

int main()
{
    int p[20], bt[20], wt[20], tat[20];
    int i, j, n, temp;
    float wtavg = 0, tatavg = 0;

    // Heading
    printf("==============================================\n");
    printf("Shortest Job First (SJF) Scheduling Algorithm\n");
    printf("==============================================\n");

    printf("\nEnter number of processes: ");
    scanf("%d", &n);

    // Input burst times
    for(i = 0; i < n; i++)
    {
        p[i] = i + 1;
        printf("Enter Burst Time for Process %d: ", i + 1);
        scanf("%d", &bt[i]);
    }

    // Sorting (SJF)
    for(i = 0; i < n - 1; i++)
    {
        for(j = i + 1; j < n; j++)
        {
            if(bt[i] > bt[j])
            {
                temp = bt[i];
                bt[i] = bt[j];
                bt[j] = temp;

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
    printf("\nPROCESS\tBT\tWT\tTAT\n");

    for(i = 0; i < n; i++)
    {
        printf("P%d\t%d\t%d\t%d\n", p[i], bt[i], wt[i], tat[i]);
    }

    printf("\nAverage Waiting Time = %.2f", wtavg / n);
    printf("Average Turnaround Time = %.2f\n", tatavg / n);

    return 0;
}