#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
    char job[10][10];
    int time[10], avail, temp[10], tem[10], safe[10];
    int i, j, n, t, q, ind = 0;

    printf("============================================\n");
    printf("Deadlock Prevention Technique\n");
    printf("============================================\n");

    printf("Enter no of jobs: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++){
        printf("Enter name and time: ");
        scanf("%s%d", job[i], &time[i]);
    }

    printf("Enter available resources: ");
    scanf("%d", &avail);

    printf("\nJobs\tTime\n");
    printf("====================\n");

    for(i = 0; i < n; i++){
        printf("%s\t%d\n", job[i], time[i]);
        temp[i] = time[i];
        tem[i] = i;
    }

    // Sorting based on time (ascending)
    for(i = 0; i < n; i++){
        for(j = i + 1; j < n; j++){
            if(temp[i] > temp[j]){
                t = temp[i]; temp[i] = temp[j]; temp[j] = t;
                t = tem[i]; tem[i] = tem[j]; tem[j] = t;
            }
        }
    }

    printf("\nExecution Order:\n");

    for(i = 0; i < n; i++){
        q = tem[i];

        if(time[q] <= avail){
            safe[ind] = q;
            printf("%s\n", job[q]);

            // 🔥 FIX: resources are released after execution
            avail = avail + time[q];

            ind++;
        }
        else{
            printf("No safe sequence\n");
            break;
        }
    }

    if(ind == n){
        printf("\nSafe sequence is: ");
        for(i = 0; i < ind; i++)
            printf("%s ", job[safe[i]]);
    }

    return 0;
}