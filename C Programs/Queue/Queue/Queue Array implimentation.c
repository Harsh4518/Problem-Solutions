#include<stdio.h>

#define N 5
int Queue[N];
int front=-1;
int rear=-1;

void Enqueue()
{
	int element;
	
	printf("\nEnter the Element to be inserted:\n");
	scanf("%d",&element);
	
	if(front==0 && rear==N-1)
	{
		printf("Queue is Full\n");
	}
	else
		if(front==-1 && rear==-1)
		{
			front=rear=0;
			Queue[rear]=element;
		}
	else
		{
			rear++;
			Queue[rear]=element;
			
		}
}

void Dequeue()
{
	if(front==-1 && rear==-1)
		{
			printf("Queue Underflow:\n");
		}
	else
		if(front==rear)
		{
			front=rear=-1;
		}
	else
		{
			printf("\nElement Dequeued:%d\n",Queue[front]);
		}	
				
}

void Display()
{
	int i;
	
	printf("\nElement Present in the Queue:\n");

	for(i=front;i<=rear;i++)
	{
		printf("\n%d ",Queue[i]);
	}
	
}

void main()
{
	int c=1,choice;
	
	printf("*****QUEUE OPERATIONS*****\n\n");
	
	printf("1.Enqueue:\n2.Dequeue:\n3.Display:\n");
	
	do
	{
		printf("\nEnter Your Choice:\n");
		scanf("%d",&choice);
		
		switch(choice)
		{
			case 1:Enqueue();
				   break;
			
			case 2:Dequeue();
				   break;
				 
			case 3:Display();
				   break;  	   
			
			default:printf("Wrong Choice:\n");
		}
		
		printf("\nDo you want to continue:1 or 0\n");
		scanf("%d",&c);
		
	}while(c==1);
}
