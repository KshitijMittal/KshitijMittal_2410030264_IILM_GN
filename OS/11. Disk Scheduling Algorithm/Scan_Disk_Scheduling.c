#include<stdio.h>
#include<stdlib.h>

int main(){
    int t[20],d[20],h,i,j,n,temp,k,atr[20],sum=0,p;

    printf("============================================\n");
    printf("SCAN Disk Scheduling Algorithm\n");
    printf("============================================\n");

    printf("Enter number of tracks: ");
    scanf("%d",&n);

    printf("Enter head position: ");
    scanf("%d",&h);

    t[0]=0;
    t[1]=h;

    printf("Enter tracks: ");
    for(i=2;i<n+2;i++)
        scanf("%d",&t[i]);

    for(i=0;i<n+2;i++){
        for(j=0;j<n+1-i;j++){
            if(t[j]>t[j+1]){
                temp=t[j];
                t[j]=t[j+1];
                t[j+1]=temp;
            }
        }
    }

    for(i=0;i<n+2;i++){
        if(t[i]==h){
            j=i;
            k=i;
            break;
        }
    }

    p=0;

    while(j>=0)
        atr[p++]=t[j--];

    for(i=k+1;i<n+2;i++)
        atr[p++]=t[i];

    for(i=0;i<n;i++){
        d[i]=atr[i+1]-atr[i];
        if(d[i]<0)
            d[i]=-d[i];
        sum+=d[i];
    }

    printf("\nAverage head movement: %f\n",(float)sum/n);

    return 0;
}