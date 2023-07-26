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
	}
	else
	{
		temp->next=newnode;
		newnode->prev=temp;
		temp=newnode;
		tail=newnode;	
	}
}

void delete_beg()
{
	if(head==0)
		
		printf("No Node for Deletion:\n");
	
	else
		{
			 temp=head;
			 head=head->next;
			 head->prev=0;
			 free(temp);
		}
		
		printf("Node Deleted At Beginning:\n");
}

void delete_end()
{
	temp=head;
   
   	while(temp->next!=0)
	{	 
		temp=temp->next;
	}
	
	if(head==0)
		printf("No Node for Deletion:\n");
	
	else
	{		
	    tail=temp->prev; 
	    temp->prev->next=0;
		free(temp);	 
	}
	
	printf("Node Deleted At the Last:\n");
}

void delete_at_position()
{
	int position,i=1;
	
	printf("Enter the postion where node is to be deleted:\n");
	scanf("%d",&position);
	
	temp=head;
	
	while(i<position)
	{	
		temp=temp->next;
		i++;
	}
	
	temp->prev->next=temp->next;
	temp->next->prev=temp->prev;
	free(temp);
	
	printf("\nNode deleted At the Position %d:",position);
	
}

void display()
{
	temp=head;
	int i=1;
	
	printf("\nElements in the Doubly Linked list Are:\n\n");
	
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
	
	printf("\n*****DELETION MENU*****\n\n");
	
	do
	  {
		printf("1.DELETION AT BEGINNING:\n2.DELETION AT END:\n3.DELETION AT A POSITION:\n");
		
		scanf("%d",&choice);
		
		printf("\n");
		
		switch(choice)
		{
			case 1:delete_beg();
		           break;
			case 2:delete_end();
			       break;
			case 3:delete_at_position();
			       break;
		    default:printf("Wrong Choice:\n");   	
		}
		
		printf("\n\nDo You Want to Continue:\n");
		scanf("%d",&choice);
		
      }while(choice==1);
      
      display();
}
