#include<stdio.h>

int main()
{
	int a,b,*x,*y,temp;
	
	printf("Enter First Number!\n");
	scanf("%d",&a);
	printf("Enter Second Number!\n");
	scanf("%d",&b);
	
	printf("\nNumber Before Swapping: %d%d",a,b);
	
	x=&a;
	y=&b;
	
	temp=*x;
	*x=*y;
	*y=temp;
	
	printf("\nNumber After Swapping: %d%d",a,b);
	
	return 0;
}
