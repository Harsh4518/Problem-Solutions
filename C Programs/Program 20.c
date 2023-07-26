#include<stdio.h>
#include<math.h>
int main()
{
	
	int i,c=0,num;
	printf("enter number:");
	scanf("%d",&num);
	
	for(i=1;i<=sqrt(num);i++)
	{
		if(num%i==0)
		c++;
    }
    
    if(c==1 && num!=1)
	 printf("\nEntered number is prime number!");
	else
	 printf("\nEntered number is not a prime a number!");
	 
	return 0; 

}
