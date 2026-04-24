#include<stdio.h>
#include<stdlib.h>

int main(){
    int t[20],n,i,tohm[20],tot=0;
    float avhm;

    printf("============================================\n");
    printf("FCFS Disk Scheduling Algorithm\n");
    printf("============================================\n");

    printf("Enter number of tracks: ");
    scanf("%d",&n);

    printf("Enter track sequence: ");
    for(i=1;i<=n;i++)
        scanf("%d",&t[i]);

    for(i=1;i<n;i++){
        tohm[i]=t[i+1]-t[i];
        if(tohm[i]<0)
            tohm[i]=-tohm[i];
    }

    for(i=1;i<n;i++)
        tot+=tohm[i];

    avhm=(float)tot/(n-1);

    printf("\nTracks\tDifference\n");
    printf("========================\n");

    for(i=1;i<n;i++)
        printf("%d\t%d\n",t[i],tohm[i]);

    printf("\nAverage head movement: %f\n",avhm);

    return 0;
}