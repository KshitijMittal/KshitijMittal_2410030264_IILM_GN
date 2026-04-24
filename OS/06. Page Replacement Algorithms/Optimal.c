#include<stdio.h>

int fr[10];

void display(int m){
    int i;
    for(i=0;i<m;i++)
        printf("%d\t",fr[i]);
    printf("\n");
}

int main(){
    int i,j,page[20],fs[10],lg[10],index,k,found,max,pf=0,n,m;

    printf("============================================\n");
    printf("Page Replacement - Optimal\n");
    printf("============================================\n");

    printf("Enter length of reference string: ");
    scanf("%d",&n);

    printf("Enter reference string: ");
    for(i=0;i<n;i++)
        scanf("%d",&page[i]);

    printf("Enter number of frames: ");
    scanf("%d",&m);

    for(i=0;i<m;i++)
        fr[i]=-1;

    for(j=0;j<n;j++){
        int flag1=0,flag2=0;

        for(i=0;i<m;i++){
            if(fr[i]==page[j]){
                flag1=flag2=1;
                break;
            }
        }

        if(flag1==0){
            for(i=0;i<m;i++){
                if(fr[i]==-1){
                    fr[i]=page[j];
                    flag2=1;
                    break;
                }
            }
        }

        if(flag2==0){
            for(i=0;i<m;i++)
                lg[i]=0;

            for(i=0;i<m;i++){
                for(k=j+1;k<n;k++){
                    if(fr[i]==page[k]){
                        lg[i]=k-j;
                        break;
                    }
                }
            }

            found=0;
            for(i=0;i<m;i++){
                if(lg[i]==0){
                    index=i;
                    found=1;
                    break;
                }
            }

            if(found==0){
                max=lg[0]; index=0;
                for(i=0;i<m;i++){
                    if(lg[i]>max){
                        max=lg[i];
                        index=i;
                    }
                }
            }

            fr[index]=page[j];
            pf++;
        }

        display(m);
    }

    printf("Total Page Faults = %d\n", pf + m);
    return 0;
}