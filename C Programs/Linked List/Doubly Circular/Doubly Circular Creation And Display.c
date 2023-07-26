#include<stdio.h>
#include<malloc.h>

struct node
{
	int data;
	struct node*next;
	struct node*prev;
};

struct node*newnode,*head=0,*tail=0,*temp;

void Create_node(int i)
{
	int element;
	
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->next=0;
	newnode->prev=0;
	
	printf("Enter the Data in the Node %d:",i);
	scanf("%d",&newnode->data);
	
	
	if(head==0 && tail==0)
	{
		temp=head=tail=newnode;
		newnode->next=head;
		newnode->prev=head;
	}
	else
	{
		temp->next=newnode;
		newnode->prev=temp;
		head->prev=newnode;
		newnode->next=head;
		temp=newnode;
		tail=newnode;	
	}
}

void display()
{
	temp=head;
	int i=1;
	
	printf("\nElements in the Doubly Circular Linked list Are:\n\n");
	
	while(temp->next!=head)
	{
		printf("Data in Node %d is %d:\n",i,temp->data);
		temp=temp->next;
		i++;
	}
	printf("Data in Node %d is %d:\n",i,temp->data);
	
}

void main()
{
	int No,i;
	
	printf("How many elements to be insterted in the linked list:\n");
	scanf("%d",&No);
	
	printf("\n");
	
	for(i=1;i<=No;i++)
	{
		Create_node(i);
	}
	
	display();
	
	printf("\nTHANK YOU!");
	
}


