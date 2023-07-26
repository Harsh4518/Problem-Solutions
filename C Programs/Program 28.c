#include<stdio.h>
int main()
{
	int num,d,sum,temp;
	
	printf("Enter any Number:\n");
	scanf("%d",&num);
	
	temp=num;
	
	while(num!=0)
	{
		d=num%10;
		sum=sum+d;
		num=num/10;
	}
	
	printf("\nSum of Digits of Number %d is %d",temp,sum);
	
	return 0;
}
