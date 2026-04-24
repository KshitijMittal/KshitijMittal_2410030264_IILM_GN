#include<stdio.h>
#include<stdlib.h>

int f[50];

int main(){
    int i, j, p, a, st, len, c;

    printf("============================================\n");
    printf("Linked File Allocation\n");
    printf("============================================\n");

    for(i=0;i<50;i++)
        f[i]=0;

    printf("\nEnter number of already allocated blocks: ");
    scanf("%d",&p);

    printf("Enter allocated block numbers: ");
    for(i=0;i<p;i++){
        scanf("%d",&a);
        f[a]=1;
    }

    do{
        printf("\nEnter starting block and length: ");
        scanf("%d %d",&st,&len);

        printf("\nLinked Allocation:\n");

        int prev = -1;

        for(j=st;j<(st+len);j++){
            if(f[j]==0){
                f[j]=1;

                if(prev != -1)
                    printf("%d -> %d\n", prev, j);

                prev = j;
            }
            else{
                printf("Block %d already allocated\n", j);
                len++;
            }
        }

        printf("End of File\n");

        printf("\nEnter 1 to continue, 0 to exit: ");
        scanf("%d",&c);

    }while(c==1);

    return 0;
}