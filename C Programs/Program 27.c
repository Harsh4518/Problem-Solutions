#include<stdio.h>
int main()
{
	int num,fact=1,i;
	
	printf("Enter Any Number:\n");
	scanf("%d",&num);
	
	for(i=1;i<=num;i++)
	{
		fact=fact*i;
	}
	
	printf("\nFactorial of Number %d is %d",num,fact);
	
	return 0;
}
