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

void delete_beg()
{
	if(head==0)
		printf("No Node Present for deletion:\n");
	else
		{
			temp=head;
			tail->next=head->next;
			head->next->prev=tail;
			head=head->next;
			free(temp);
		}	
		
		printf("\nNode Deleted At the Beginning:\n");

}

void delete_end()
{
	if(head==0)
		printf("No Node Present for deletion:\n");
	else
		{
			temp=tail;
			head->prev=tail->prev;
			tail->prev->next=head;
			tail=tail->prev;
			free(temp);
		}
		
		printf("\nNode Deleted at the last Position:\n");	
}

void delete_at_position()
{
   int position,i=1;
   
   temp=head;
   
   printf("\nEnter the Position where node is to be deleted:\n");
   scanf("%d",&position);
   
   while(i<position)
   {
   		temp=temp->next;
   		i++;
   }
   
   temp->prev->next=temp->next;
   temp->next->prev=temp->prev;
   
   printf("\nNode deleted of the Position %d:\n",position);
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
	printf("1.DELETION AT BEGINNING:\n2.DELETION AT END:\n3.DELETION AT A GIVEN POSITION:\n");
	
	do
	{	
		printf("\nENTER YOUR CHOICE:\n");
		scanf("%d",&choice);
		
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
		
		printf("\nDo you want to continue:1 or 0:\n");
		scanf("%d",&c);
	
	}while(c==1);
	
	display();
	
}
	
	


