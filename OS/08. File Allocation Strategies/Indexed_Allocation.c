#include<stdio.h>
#include<stdlib.h>

int f[50];

int main(){
    int i, k, j, inde[50], n, c, p;

    printf("============================================\n");
    printf("Indexed File Allocation\n");
    printf("============================================\n");

    for(i=0;i<50;i++)
        f[i]=0;

    do{
        printf("\nEnter index block: ");
        scanf("%d",&p);

        if(f[p]==1){
            printf("Index block already allocated\n");
            continue;
        }

        f[p]=1;

        printf("Enter number of blocks for file: ");
        scanf("%d",&n);

        printf("Enter block numbers:\n");
        for(i=0;i<n;i++)
            scanf("%d",&inde[i]);

        for(i=0;i<n;i++){
            if(f[inde[i]]==1){
                printf("Block %d already allocated\n", inde[i]);
                break;
            }
        }

        if(i==n){
            for(j=0;j<n;j++)
                f[inde[j]]=1;

            printf("\nFile Allocation:\n");
            printf("Index Block: %d\n", p);

            for(k=0;k<n;k++)
                printf("Block %d -> Allocated\n", inde[k]);
        }

        printf("\nEnter 1 to continue, 0 to exit: ");
        scanf("%d",&c);

    }while(c==1);

    return 0;
}