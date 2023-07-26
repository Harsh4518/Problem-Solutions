#include<stdio.h>

int Reverse(int);

int main()
{
	int N,Rev;
	
	printf("Enter Any Number:\n");
	scanf("%d",&N);
	
	Rev=Reverse(N);
	
	printf("Reverse of Number %d is: %d",N,Rev);
	
	return 0;
}

int sum=0,r;

int Reverse(int N)
{
	
	if(N!=0)
	
	{
	 r=N%10;
	 sum=sum*10+r;
	 Reverse(N/10);
    }
    
	else
     
     return 0;
	
   return sum;
}
