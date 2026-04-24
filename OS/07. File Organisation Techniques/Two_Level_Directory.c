#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct{
    char dname[10], fname[10][10];
    int fcnt;
}dir[10];

int main(){
    int i,ch,dcnt=0,k;
    char f[30],d[30];

    printf("============================================\n");
    printf("Two Level Directory\n");
    printf("============================================\n");

    while(1){
        printf("\n1.Create Directory 2.Create File 3.Delete File 4.Search File 5.Display 6.Exit");
        printf("\nEnter choice-- ");
        scanf("%d",&ch);

        switch(ch){

            case 1:
                printf("Enter directory name-- ");
                scanf("%s",dir[dcnt].dname);
                dir[dcnt].fcnt=0;
                dcnt++;
                printf("Directory created\n");
                break;

            case 2:
                printf("Enter directory name-- ");
                scanf("%s",d);
                for(i=0;i<dcnt;i++){
                    if(strcmp(d,dir[i].dname)==0){
                        printf("Enter file name-- ");
                        scanf("%s",dir[i].fname[dir[i].fcnt]);
                        dir[i].fcnt++;
                        printf("File created\n");
                        break;
                    }
                }
                if(i==dcnt) printf("Directory not found\n");
                break;

            case 3:
                printf("Enter directory name-- ");
                scanf("%s",d);
                for(i=0;i<dcnt;i++){
                    if(strcmp(d,dir[i].dname)==0){
                        printf("Enter file name-- ");
                        scanf("%s",f);
                        for(k=0;k<dir[i].fcnt;k++){
                            if(strcmp(f,dir[i].fname[k])==0){
                                printf("File %s deleted\n",f);
                                strcpy(dir[i].fname[k],dir[i].fname[dir[i].fcnt-1]);
                                dir[i].fcnt--;
                                break;
                            }
                        }
                        break;
                    }
                }
                if(i==dcnt) printf("Directory not found\n");
                break;

            case 4:
                printf("Enter directory name-- ");
                scanf("%s",d);
                for(i=0;i<dcnt;i++){
                    if(strcmp(d,dir[i].dname)==0){
                        printf("Enter file name-- ");
                        scanf("%s",f);
                        for(k=0;k<dir[i].fcnt;k++){
                            if(strcmp(f,dir[i].fname[k])==0){
                                printf("File found\n");
                                break;
                            }
                        }
                        break;
                    }
                }
                if(i==dcnt) printf("Directory not found");
                break;

            case 5:
                if(dcnt==0) printf("No directories");
                else{
                    printf("\nDirectory\tFiles");
                    for(i=0;i<dcnt;i++){
                        printf("\n%s\t",dir[i].dname);
                        for(k=0;k<dir[i].fcnt;k++)
                            printf("\t%s",dir[i].fname[k]);
                    }
                }
                printf("\n");
                break;

            case 6:
                exit(0);

            default:
                printf("Invalid choice");
        }
    }
}