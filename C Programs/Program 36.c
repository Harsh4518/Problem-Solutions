#include<stdio.h>

int factorial(int);

int main()
{
	int Factorial,Num;
	
	printf("Enter Number Whose Factorial is to be Find:\n");
	scanf("%d",&Num);
	
	Factorial=factorial(Num);
	
	printf("\nFactorial of a given number %d is: %d",Num,Factorial);
	
	return 0;
}

int factorial(int a)

{
	int i,fact=1;
	
	for(i=1;i<=a;i++)
	 
	 {
	 	 fact=fact*i;
     }
	
	return fact;
	
}
