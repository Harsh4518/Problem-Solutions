#include<stdio.h>
main()
{
	int num,d1,d2,d3,temp;
	printf("enter a number\n");
	scanf("%3d",&num);
	temp=num;
	
	d1=num%10;
	num=num/10;
	d2=num%10;
	num=num/10;
	d3=num%10;
	num=num/10;

	printf("\nSum of digits of Number %3d =%d",temp,(d1+d2+d3));
	
	return 0;
	
	
	
	
	
	
}
