#include<stdio.h>
int main()
{
	int a,b;
	printf("enter first number\n");
	scanf("%d",&a);
	printf("enter second number\n");
	scanf("%d",&b);
	
	a=a+b;
	b=a-b;
	a=a-b;
	
	printf("\nnumbers after swapping=%d%d",a,b);
	
	return 0;
}
	

