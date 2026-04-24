#include<stdio.h>
#include<stdlib.h>

int main(){
    int t[20],d[20],h,i,j,n,temp,k,atr[20],sum=0,tot,p;

    printf("============================================\n");
    printf("C-SCAN Disk Scheduling Algorithm\n");
    printf("============================================\n");

    printf("Enter number of tracks to be traversed: ");
    scanf("%d",&n);

    printf("Enter head position: ");
    scanf("%d",&h);

    printf("Enter total disk size: ");
    scanf("%d",&tot);

    t[0]=0;
    t[1]=h;
    t[2]=tot-1;

    printf("Enter tracks: ");
    for(i=3;i<n+3;i++)
        scanf("%d",&t[i]);

    for(i=0;i<n+3;i++){
        for(j=0;j<n+2-i;j++){
            if(t[j]>t[j+1]){
                temp=t[j];
                t[j]=t[j+1];
                t[j+1]=temp;
            }
        }
    }

    for(i=0;i<n+3;i++){
        if(t[i]==h){
            j=i;
            break;
        }
    }

    p=0;

    for(i=j;i<n+3;i++)
        atr[p++]=t[i];

    for(i=0;i<j;i++)
        atr[p++]=t[i];

    for(i=0;i<n+2;i++){
        d[i]=atr[i+1]-atr[i];
        if(d[i]<0)
            d[i]=-d[i];
        sum+=d[i];
    }

    printf("\nTotal head movement: %d\n",sum);
    printf("Average head movement: %f\n",(float)sum/n);

    return 0;
}