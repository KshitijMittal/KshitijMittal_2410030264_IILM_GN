#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(){
    int alloc[10][10],max[10][10],avail[10],work[10],need[10][10],total[10];
    int i,j,k,n,m,count=0,c;
    char finish[10];

    printf("============================================\n");
    printf("Banker's Algorithm - Deadlock Avoidance\n");
    printf("============================================\n");

    printf("Enter processes and resources: ");
    scanf("%d%d",&n,&m);

    for(i=0;i<n;i++)
        finish[i]='n';

    printf("Enter claim matrix:\n");
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            scanf("%d",&max[i][j]);

    printf("Enter allocation matrix:\n");
    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            scanf("%d",&alloc[i][j]);

    printf("Enter resource vector:\n");
    for(i=0;i<m;i++)
        scanf("%d",&total[i]);
    printf("\n");

    for(i=0;i<m;i++)
        avail[i]=0;

    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            avail[j]+=alloc[i][j];

    for(i=0;i<m;i++)
        work[i]=total[i]-avail[i];

    for(i=0;i<n;i++)
        for(j=0;j<m;j++)
            need[i][j]=max[i][j]-alloc[i][j];

A:
    for(i=0;i<n;i++){
        c=0;
        for(j=0;j<m;j++){
            if(need[i][j]<=work[j] && finish[i]=='n')
                c++;
        }
        if(c==m){
            printf("Process %d executed\n",i+1);
            for(k=0;k<m;k++)
                work[k]+=alloc[i][k];
            finish[i]='y';
            count++;
        }
    }

    if(count!=n)
        goto A;

    printf("System is in safe state\n");

    return 0;
}