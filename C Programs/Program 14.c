#include<stdio.h>
main()
{
	int num,d1,d2,d3,temp;
	printf("enter value of a number\n");
	scanf("%d",&num);
	temp=num;
	
	d1=num%10;
	num=num/10;
	d2=num%10;
	num=num/10;
	d3=num%10;
	num=num/10;
	
	printf("\nreverse of number %d=%d%d%d",temp,d1,d2,d3);
	
	return 0;
	
}
