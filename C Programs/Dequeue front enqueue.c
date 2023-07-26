#include<stdio.h>

#define N 5
int deQueue[N];
int front=-1;
int rear=-1;

void Enqueue_front(int X)
{
	if(front==0 && rear==N-1)
	{
		printf("Queue overflow\n");
			
	}
else 
    if(front==-1 && rear==-1)
    {
    	front=0;
    	rear=0;
    	deQueue[front]=X;
	}
else
    if(front==0)
    {
    	front=N-1;
    	deQueue[front]=X;
    }
    else
    {
    	front--;
    	deQueue[front]=X;
	}
}

void display()
{
	int i=front;
	
	printf("Elements of Queue\n");
	
	while(i!=rear)
	{
		printf("%d",deQueue[i]);
		
		i=(i+1)%N;
	}
	
	printf("%d",deQueue[i]);
}

int main()
{
	Enqueue_front(1);
	Enqueue_front(1);
	Enqueue_front(1);
	Enqueue_front(1);
	Enqueue_front(1);
	
	display();
	
	return 0;
	
}
	
	

