#include<stdio.h>
#include<stdlib.h>

int main(){
    int f[50], i, st, j, len, c;

    printf("============================================\n");
    printf("Sequential File Allocation\n");
    printf("============================================\n");

    for(i=0;i<50;i++)
        f[i]=0;

    do{
        printf("\nEnter starting block and length of file: ");
        scanf("%d %d",&st,&len);

        printf("\nAllocated Blocks:\n");

        for(j=st;j<(st+len);j++){
            if(f[j]==0){
                f[j]=1;
                printf("Block %d -> Allocated\n", j);
            }
            else{
                printf("Block %d -> Already Allocated\n", j);
                break;
            }
        }

        if(j==(st+len))
            printf("File allocated successfully\n");

        printf("\nDo you want to enter more files? (1-Yes / 0-No): ");
        scanf("%d",&c);

    }while(c==1);

    return 0;
}