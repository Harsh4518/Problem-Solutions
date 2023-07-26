#include<stdio.h>
#include<math.h>

int factorial(int);

int main()
{
	int i,n;
	float sum=0.0;
	
	printf("Enter Value of N:\n");
	scanf("%d",&n);
	
	for(i=1;i<=n;i++)
	{
		sum=sum+pow(-1,i+1)*(float)i/factorial(2*i-1);
	}
	
    printf("\nSum of Series Upto %d Terms: %.2f",n,sum);
    
    return 0;
}

int factorial(int x)
{
	int a,fact=1;
	
	for(a=1;a<=x;a++)
	{
		fact=fact*a;
	}
	
	return fact;
}
