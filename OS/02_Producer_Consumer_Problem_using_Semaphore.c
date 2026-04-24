#include <stdio.h>
#include <stdlib.h>

int mutex = 1, full = 0, empty = 10;
int buffer[10];
int in = 0, out = 0;

// Wait operation
void wait(int *s)
{
    (*s)--;
}

// Signal operation
void signal(int *s)
{
    (*s)++;
}

void producer()
{
    int item;

    if(empty == 0)
    {
        printf("\nBuffer is Full\n");
        return;
    }

    printf("\nEnter item to produce: ");
    scanf("%d", &item);

    wait(&empty);
    wait(&mutex);

    buffer[in] = item;
    printf("Produced item: %d\n", item);

    in = (in + 1) % 10;

    signal(&mutex);
    signal(&full);
}

void consumer()
{
    int item;

    if(full == 0)
    {
        printf("\nBuffer is Empty\n");
        return;
    }

    wait(&full);
    wait(&mutex);

    item = buffer[out];
    printf("\nConsumed item: %d\n", item);

    out = (out + 1) % 10;

    signal(&mutex);
    signal(&empty);
}

int main()
{
    int choice;

    printf("============================================\n");
    printf("Producer Consumer Problem using Semaphores\n");
    printf("============================================\n");

    while(1)
    {
        printf("\n1. Produce \t 2. Consume \t 3. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice)
        {
            case 1: producer(); break;
            case 2: consumer(); break;
            case 3: exit(0);
            default: printf("\nInvalid Choice\n");
        }
    }

    return 0;
}