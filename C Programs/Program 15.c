#include<stdio.h>
main()
{
	int num;
	printf("enter a number \n");
	scanf("%d",&num);
	
	(num%2==0?printf("\n%d is an even number",num):printf("\n%d is an odd number",num));
	
	return 0;
	
	
}
