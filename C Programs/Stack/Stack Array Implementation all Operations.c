#include<stdio.h>

#define N 5
int Stack[N];
int top=-1;

void Push()
{
	int element;
	
	printf("\nEnter the element to be inserted:\n");
	scanf("%d",&element);
	
	if(top==N-1)
		printf("Stack is Overflow No more space for insertion present:\n");
	else
		{
			top++;
			Stack[top]=element;
		}
		
		printf("\nElement Inserted At the Top:%d\n",top);	
	
}

void Pop()
{
	if(top==-1)
		printf("Stack Underflow no element present for deletion:\n");
	else
		{
			printf("\nDeleted Element from the stack is:%d\n",Stack[top]);
			top--;
		}
		
		printf("\nElement Popped:\n");	
}

void isempty()
{
	if(top==-1)
		printf("Stack is Completely empty,no element present in stack:\n");
	else
		printf("Stack is not empty,element present in stack:\n");	
}

void isfull()
{
	if(top==N-1)
		printf("Stack is Full,No More space Present:\n");
	else
		printf("Stack is not full,space available in stack:\n");	
}

void peek()
{
	if(top==-1)
		printf("Stack is Completely empty,no element present in stack:\n");
	else
		printf("Element present at the top of stack:%d\n",Stack[top]);	
	
}

void display()
{
	int i;
	
	if(top==-1)
		printf("Stack Underflow,No element present in stack:\n");
	else
		{
			printf("\nElements in the Stack:\n");
			
			for(i=top;i>=0;i--)
			{
				printf("\nAt Top=%d Element is:%d",i,Stack[i]);
			}
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
				
			case 5:isfull();
			       break;
			       
			case 6:display();
			       break;
			       
			default:printf("WRONG CHOICE:\n");       
		}
		
		printf("\nDo you want to continue:1 or 0\n");
		scanf("%d",&c);
	
	}while(c==1);

}
