#include<stdio.h>

int Sum(int);

int main()
{
	int N,Result;
	
	printf("Enter Any Number:\n");
	scanf("%d",&N);
	
	Result=Sum(N);
	
	printf("Sum of Digits of Number %d is: %d",N,Result);
	
	return 0;
}

int Sum(int N)
{
	if(N==0)
	 
	 return 0;
	
	else 
	 
	 return( Sum(N/10)+N%10);
	  
}

