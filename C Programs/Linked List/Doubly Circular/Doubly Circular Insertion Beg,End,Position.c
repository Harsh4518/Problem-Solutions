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

void insert_beg()
{
   newnode=(struct node*)malloc(sizeof(struct node));
   newnode->next=0;
   newnode->prev=0;
   
   printf("\nEnter the Data in the Node:\n");
   scanf("%d",&newnode->data);
   
   newnode->next=head;
   newnode->prev=tail;
   head->prev=newnode;
   tail->next=newnode;
   head=newnode;
   
   printf("\nNode Inserted at the beginning:\n");
}

void insert_end()
{
   newnode=(struct node*)malloc(sizeof(struct node));
   newnode->next=0;
   newnode->prev=0;
   
   printf("\nEnter the Data in the Node:\n");
   scanf("%d",&newnode->data);
   
   tail->next=newnode;
   newnode->prev=tail;
   newnode->next=head;
   head->prev=newnode;
   tail=newnode;
   
   printf("\nNode Inserted at the end:\n");
}

void insert_at_position()
{
   int position,i=1;
   
   temp=head;
   
   printf("\nEnter the Position where node is to be inserted:\n");
   scanf("%d",&position);
	 
   newnode=(struct node*)malloc(sizeof(struct node));
   newnode->next=0;
   newnode->prev=0;
   
   printf("\nEnter the Data in the Node:\n");
   scanf("%d",&newnode->data);
   
   while(i<position)
   {
   		temp=temp->next;
   		i++;
   }
   
   newnode->prev=temp;
   newnode->next=temp->next;
   temp->next->prev=newnode;
   temp->next=newnode;
   
   printf("\nNode Inserted after the Position %d:\n",position);
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
	int No,i,choice=1,c;
	
	printf("How many elements to be insterted in the linked list:\n");
	scanf("%d",&No);
	
	printf("\n");
	
	for(i=1;i<=No;i++)
	{
		Create_node(i);
	}
	
	printf("\n*****INSERTION MENU******\n\n");
	printf("1.INSERTION AT BEGINNING:\n2.INSERTION AT END:\n3.INSERTION AT A GIVEN POSITION:\n");
	
	do
	{	
		printf("\nENTER YOUR CHOICE:\n");
		scanf("%d",&choice);
		
		switch(choice)
		{
			case 1:insert_beg();
				   break;
				   
			case 2:insert_end();
				   break;
				   
			case 3:insert_at_position();
				   break;
			
			default:printf("Wrong Choice:\n");	   
		}
		
		printf("\nDo you want to continue:1 or 0:\n");
		scanf("%d",&c);
	
	}while(c==1);
	
	display();
	
}
	
	


