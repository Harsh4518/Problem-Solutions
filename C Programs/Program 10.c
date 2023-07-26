#include<stdio.h>
main()
{
	int x,y,z,c1,c2;
	printf("enter first number \n");
	scanf("%d",&x);
	printf("enter second number \n");
	scanf("%d",&y);
	printf("enter third number \n");
	scanf("%d",&z);
	
	c1=x;
	c2=z;\
	x=c2;
	z=c1;
	
	
	printf("\n number after swapping=%d%d%d",x,y,z);
	
	return 0;
}
