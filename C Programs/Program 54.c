#include<stdio.h>

int FIB(int);

int main()
{
	int N,i;
	
	printf("Enter Any Number:\n");
	scanf("%d",&N);
	
	printf("Fibonacci Series for Number %d is:",N);
	
	for(i=1;i<=N;i++)
	{
		printf(" %d ",FIB(i));
	}
	
	return 0;
}

int FIB(int n)
{
	if(n==1)
	 
	 return 0;
	
	else
	 
	 if(n==2)
	  
	  return 1;
	
	else
	 
	 return FIB(n-1)+FIB(n-2);  
}
