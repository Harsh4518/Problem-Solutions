#include<stdio.h>
#include<malloc.h>

struct node
{
	int data;
	struct node*next;
};

struct node*newnode,*head=0,*tail=0,*temp;

void Create_node(int i)
{
	int element;
	
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->next=0;
	
	printf("Enter the Data in the Node %d:",i);
	scanf("%d",&newnode->data);
	
	
	if(head==0)
	{
		temp=head=tail=newnode;
		newnode->next=head;
	}
	else
	{
		temp->next=newnode;
		newnode->next=head;
		temp=tail=newnode;	
	}
}

void display()
{
	temp=head;
	int i=1;
	
	printf("\nElements in the Singly Circular Linked list Are:\n\n");
	
	while(temp->next!=head)
	{
		printf("Data in Node %d is %d:\n",i,temp->data);
		temp=temp->next;
		i++;
	}
	printf("Data in Node %d is %d:\n",i,temp->data);
	
}

int main()
{
	int c,i;
	
	printf("How many Elements You want to insert:\n");
	scanf("%d",&c);
	
	printf("\n");
	
	for(i=1;i<=c;i++)
	{
		Create_node(i);
	}
	
	display();
	
	printf("\nThank You!");
	
	
}
