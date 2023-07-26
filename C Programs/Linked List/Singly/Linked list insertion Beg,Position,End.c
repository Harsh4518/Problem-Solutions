#include<stdio.h>
#include<malloc.h>

struct node
{
	int data;
	struct node*next;
};

struct node*newnode,*head=0,*temp;

void Create_node(int i)
{
	int element;
	
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->next=0;
	
	printf("Enter the Data in the Node %d:",i);
	scanf("%d",&newnode->data);
	
	
	if(head==0)
	{
		temp=head=newnode;
	}
	else
	{
		temp->next=newnode;
		temp=newnode;	
	}
}

void insert_beg()
{
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->next=0;
	
	printf("Enter the Data in the Newnode:\n");
	scanf("%d",&newnode->data);
	
	newnode->next=head;
	head=newnode;
	
	printf("Node inserted at the beginning:\n");
	
}

void insert_end()
{
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->next=0;
	
	printf("Enter the Data in the Newnode:\n");
	scanf("%d",&newnode->data);
	
	temp=head;
	
	while(temp->next!=0)
	{
		temp=temp->next;
	}
	
	temp->next=newnode;
	
	printf("Node insterted at the End of linked list:\n");
	

}

void insert_at_position()
{
	int position,i=1;
	
	printf("Enter the postion where node is to be inserted:\n");
	scanf("%d",&position);
	
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->next=0;
	
	printf("Enter the Data in the Newnode:\n");
	scanf("%d",&newnode->data);	
	
	temp=head;
	
	while(i<position)
	{
		temp=temp->next;
		i++;
	}
	
	newnode->next=temp->next;
	temp->next=newnode;
	
	printf("Node inserted At the Position %d:",position);
	
}

void display()
{
	temp=head;
	int i=1;
	
	printf("\nElements in the Singly Linked list Are:\n\n");
	
	while(temp->next!=0)
	{
		printf("Data in Node %d is %d:\n",i,temp->data);
		temp=temp->next;
		i++;
	}
	printf("Data in Node %d is %d:\n",i,temp->data);
	
}

void main()
{
	int c,i,choice=1;
	
	printf("How many Elements You want to insert:\n");
	scanf("%d",&c);
	
	printf("\n");
	
	for(i=1;i<=c;i++)
	{
		Create_node(i);
	}
	
	printf("\n*****INSERTION MENU*****\n\n");
	
	do
	  {
		printf("1.INSERT AT BEGINNING:\n2.INSERT AT END:\n3.INSERT AT A POSITION:\n");
		
		scanf("%d",&choice);
		
		printf("\n");
		
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
		
		printf("\n\nDo You Want to Continue:\n");
		scanf("%d",&choice);
		
      }while(choice==1);
      
      display();
}
