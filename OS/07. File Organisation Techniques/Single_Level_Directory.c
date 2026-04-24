#include<stdio.h>
#include<string.h>

struct{
    char dname[10], fname[10][10];
    int fcnt;
}dir;

int main(){
    int i, ch;
    char f[30];

    printf("============================================\n");
    printf("Single Level Directory\n");
    printf("============================================\n");

    dir.fcnt = 0;

    printf("Enter name of directory-- ");
    scanf("%s", dir.dname);

    while(1){
        printf("\n1.Create File\t2.Delete File\t3.Search File\t4.Display Files\t5.Exit");
        printf("\nEnter choice-- ");
        scanf("%d",&ch);

        switch(ch){

            case 1:
                printf("Enter file name-- ");
                scanf("%s", dir.fname[dir.fcnt]);
                dir.fcnt++;
                break;

            case 2:{
                int found = 0;
                printf("Enter file name-- ");
                scanf("%s", f);
                for(i=0;i<dir.fcnt;i++){
                    if(strcmp(f,dir.fname[i])==0){
                        printf("File %s deleted",f);
                        strcpy(dir.fname[i],dir.fname[dir.fcnt-1]);
                        dir.fcnt--;
                        found = 1;
                        break;
                    }
                }
                printf("\n");
                if(!found) printf("File not found\n");
                break;
            }

            case 3:
                printf("Enter file name-- ");
                scanf("%s", f);
                for(i=0;i<dir.fcnt;i++){
                    if(strcmp(f,dir.fname[i])==0){
                        printf("File %s found",f);
                        break;
                    }
                }
                printf("\n");
                if(i==dir.fcnt) printf("File not found\n");
                break;

            case 4:
                if(dir.fcnt==0) printf("Directory empty\n");
                else{
                    printf("Files:");
                    for(i=0;i<dir.fcnt;i++)
                        printf("\n%s",dir.fname[i]);
                }
                printf("\n");
                break;

            case 5:
                return 0;

            default:
                printf("Invalid choice");
        }
    }
}