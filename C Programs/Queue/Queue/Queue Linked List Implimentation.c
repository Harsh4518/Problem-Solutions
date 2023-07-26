#include<stdio.h>
#include<malloc.h>

struct node
{
	int data;
	struct node *next;
};

struct node *newnode,*front=0,*rear=0,*temp;

void Enqueue()
{
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->next=0;
	
	printf("\nEnter the Data:\n");
	scanf("%d",&newnode->data);
	
	if(front==0 && rear==0)
	{
		front=rear=newnode;
	}
	else
		{
			rear->next=newnode;
			rear=newnode;
		}
}

void dequeue()
{
	temp=front;
	
	if(front==0 && rear==0)
		printf("Queue Underflow:\n");
	else
		if(front==rear)
		{
			front=rear=0;
			free(temp);
		}
	else
		{
			front=front->next;
			printf("\nEnqueued Element:%d\n",temp->data);
			free(temp);			
		}	
	
}

void display()
{
	temp=front;
	
	if(front==0 && rear==0)
		printf("Queue Underflow:\n");
		
	else
		{
			printf("\nElement in The Queue:\n");
			
			while(temp!=rear)
			{
				
				printf("\nData:%d\n",temp->data);
				temp=temp->next;
			}
			
			printf("\nData:%d\n",temp->data);
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
		
			case 2:dequeue();
				   break;
				 
			case 3:display();
				   break;  	   
			
			default:printf("Wrong Choice:\n");
		}
		
		printf("\nDo you want to continue:1 or 0\n");
		scanf("%d",&c);
		
	}while(c==1);
}


