#include<stdio.h>
int main()
{
	int a,b,temp;
	printf("enter first number\n");
	scanf("%d",&a);
	printf("enter second number\n");
	scanf("%d",&b);
	
	temp=a;
	a=b;
	b=temp;
	
	printf("\nnumbers after swapping=%d%d",a,b);
	
	return 0;
}
	
