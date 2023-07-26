#include<stdio.h>
#include<math.h>
int main()
{
	int num,i,count=0;
	
	printf("Enter any Number:\n");
	scanf("%d",&num);
	
	for(i=1;i<=sqrt(num);i++)
	{
		if(num%i==0)
		count++;
	}
	
	if(count==1 && num!=1)
	 
	 printf("\nEntered Number %d is a Prime Number!",num);
	 
	else
	
	 printf("\nEntered Number %d is not a Prime Number!",num);
	 
	return 0;  
	
}
