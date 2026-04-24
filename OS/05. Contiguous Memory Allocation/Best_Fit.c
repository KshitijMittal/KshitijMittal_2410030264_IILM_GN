#include<stdio.h>
#define max 25

int main(){
int frag[max],b[max],f[max],bf[max]={0},ff[max]={0};
int i,j,nb,nf,temp,lowest;

printf("============================================\n");
printf("Memory Allocation - Best Fit\n");
printf("============================================\n");

printf("Enter number of blocks: ");
scanf("%d",&nb);

printf("Enter number of files: ");
scanf("%d",&nf);

printf("\nEnter block sizes:\n");
for(i=1;i<=nb;i++){
    printf("Block %d: ",i);
    scanf("%d",&b[i]);
}

printf("\nEnter file sizes:\n");
for(i=1;i<=nf;i++){
    printf("File %d: ",i);
    scanf("%d",&f[i]);
}

for(i=1;i<=nf;i++){
    lowest=9999;

    for(j=1;j<=nb;j++){
        if(bf[j]==0){
            temp=b[j]-f[i];
            if(temp>=0 && temp<lowest){
                ff[i]=j;
                lowest=temp;
            }
        }
    }

    if(ff[i]!=0){
        frag[i]=lowest;
        bf[ff[i]]=1;
    }
    else frag[i]=-1;
}

printf("\nFile\tSize\tBlock\tBlockSize\tFragment\n");
for(i=1;i<=nf;i++){
    if(ff[i]!=0)
        printf("%d\t%d\t%d\t%d\t\t%d\n",i,f[i],ff[i],b[ff[i]],frag[i]);
    else
        printf("%d\t%d\tNot Allocated\n",i,f[i]);
}

return 0;
}