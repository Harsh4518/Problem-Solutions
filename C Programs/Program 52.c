#include<stdio.h>

int Factorial(int);

int main()
{
	int N;
	
	printf("Enter Any Number:\n");
	scanf("%d",&N);
	
	printf("Factorial of Number %d is: %d\n",N,Factorial(N));
	
	return 0;
}

int Factorial(int N)
{
	if(N==0)
	 
	 return 1;
	
	else 
	 
	 return N*Factorial(N-1); 
}
