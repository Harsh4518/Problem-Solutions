#include<stdio.h>
#include<math.h>
int main()
{
	int num,i,count=0;
	char choice;
	
	printf("Enter any Number:\n");
	scanf("%d",&num);
do
{
		
	for(i=1,count=0;i<=sqrt(num);i++)
	{
		if(num%i==0)
		count++;
	}
	
	if(count==1 && num!=1)
	 
	 printf("\nEntered Number %d is a Prime Number!",num);
	 
	else
	
	 printf("\nEntered Number %d is not a Prime Number!",num);
	 
	 
	 printf("\n\n\nDo You want to Continue!...Please Enter Your Choice Either (Y/N):\n");
	 fflush(stdin);
	 scanf("%c",&choice);
	 
	printf("\n\n\nEnter any Number:\n");
	scanf("%d",&num);
	 
}while( choice=='y' || choice=='Y');

     printf("\n\n\n***TASK IS OVER!***");
	
	 return 0;  
	
}
