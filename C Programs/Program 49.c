#include<stdio.h>
#include<math.h>

int factorial(int);

int main()
{
	int i,n,x;
	float sum=0.0;
	
	printf("Enter Value of N:\n");
	scanf("%d",&n);
	printf("Enter Any Value of X:\n");
	scanf("%d",&x);
		
	for(i=1;i<=n;i++)
	{
		sum=sum+pow(x,2*i-1)/factorial(2*i-1);
	}
	
    printf("\nSum of Series Upto %d Terms when value of X is %d: %.2f",n,x,sum);
    
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
