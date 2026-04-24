#include <stdio.h>

int main()
{
    int bt[20], wt[20], tat[20];
    int i, n;
    float wtavg = 0, tatavg = 0;

    printf("============================================\n");
    printf("First Come First Serve Scheduling Algorithm\n");
    printf("============================================\n");

    printf("Enter number of processes: ");
    scanf("%d", &n);

    // Input burst times
    for(i = 0; i < n; i++)
    {
        printf("Enter Burst Time for Process %d: ", i + 1);
        scanf("%d", &bt[i]);
    }

    // Calculation logic
    wt[0] = 0; // First process doesn't wait
    tat[0] = bt[0];

    for(i = 1; i < n; i++)
    {
        wt[i] = wt[i-1] + bt[i-1];
        tat[i] = wt[i] + bt[i]; // TAT = WT + BT
    }

    // Output table
    printf("\nPROCESS\tBT\tWT\tTAT\n");
    for(i = 0; i < n; i++)
    {
        printf("P%d\t%d\t%d\t%d\n", i + 1, bt[i], wt[i], tat[i]);
        wtavg += wt[i];
        tatavg += tat[i];
    }

    printf("\nAverage Waiting Time = %.2f", wtavg / n);
    printf("\nAverage Turnaround Time = %.2f\n", tatavg / n);

    return 0;
}
