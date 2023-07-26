#include<stdio.h>
#include<malloc.h>

struct node
{
	int data;
	struct node *next;
};

struct node *top=0,*newnode,*temp;

void Push()
{
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->next=0;
	
	printf("\nEnter the Element to inserted:\n");
	scanf("%d",&newnode->data);
	
	if(top==0)
		{
			top=newnode;
		}
	else
		{
			newnode->next=top;
			top=newnode;
		}	
}

void Pop()
{
	if(top==0)
		printf("Stack Underflow,no element for deletion:\n");
	
	else
		{
			temp=top;
			top=top->next;
			printf("\nPopped Element:%d\n",temp->data);
			free(temp);
		}	
}

void isempty()
{
	if(top==0)
		printf("\nStack is Completely empty,no element present in stack:\n");
	else
		printf("\nStack is not empty,element present in stack:\n");	
}

void peek()
{
	if(top==0)
		printf("\nStack is Completely empty,no element present in stack:\n");
	else
		printf("\nElement present at the top of stack:%d\n",top->data);	
	
}

void display()
{
	int i=1; 
	
	if(top==0)
		printf("Stack is Completely empty,no element present in stack:\n");
	else
		{
			temp=top;
			
			printf("\nELEMENTS OF STACK:\n\n");
			
			while(temp->next!=0)
			{
				printf("Element %d is %d:\n",i++,temp->data);
				temp=temp->next;
			}
			
			printf("Element %d is %d:\n",i++,temp->data);
			
		}	
}

void main()
{
	int c=1,choice;
	
	printf("*****STACK OPERATIONS MENU*****\n\n");
	printf("1.PUSH:\n2.POP:\n3.PEEK:\n4.ISEMPTY:\n5.ISFULL:\n6.DISPLAY:\n");
	
	do
	{
		printf("\nEnter Your Choice:\n");
		scanf("%d",&choice);
		
		switch(choice)
		{
			case 1:Push();
			       break;
			       
			case 2:Pop();
			       break;
			       
			case 3:peek();
			       break;
				   
			case 4:isempty();
			       break;
			       
			case 5:display();
			       break;
			       
			default:printf("WRONG CHOICE:\n");       
		}
		
		printf("\nDo you want to continue:1 or 0\n");
		scanf("%d",&c);
	
	}while(c==1);
}

