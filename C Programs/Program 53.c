#include<stdio.h>

int Combination(int,int);

int Factorial(int);

int main()
{
	int N,R,Result;
	
	printf("Enter Value of N:\n");
	scanf("%d",&N);
	
	printf("Enter Value of R:\n");
	scanf("%d",&R);
	
	Result=Combination(N,R);
	
	printf("Total Number of Combination Possible With N=%d And R=%d is: %d",N,R,Result);
	
	return 0;
}

int Factorial(int N)
{
	int i,fact=1;
	
	for(i=1;i<=N;i++)
	{
		fact=fact*i;
	}
	
	return fact;
}

int Combination(int N,int R)
{
	int C;
	
	C=Factorial(N)/(Factorial(N-R)*Factorial(R));
	
	return C;
}
