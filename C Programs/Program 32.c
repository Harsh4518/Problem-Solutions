#include<stdio.h>
int main()
{
	int num,sum=0,i,temp;
	
	printf("Enter any Number:");
	scanf("%d",&num);
	
	temp=num;
	
	for(i=1;i<=num/2;i++)
	{
		if(num%i==0)
		sum=sum+i;	
	}
	
	if(sum==temp)
	
	 printf("\nEntered Number %d is a Perfect Number!",num);
	 
	else
	 
	 printf("\nEntered Number %d is not a Perfect Number!",num);
	 
	return 0;  
	 
}

