#include<stdio.h>
main()
{
	int v,u,a,t;
	printf("enter value of initial velocity \n");
	scanf("%d",&u);
	printf("enter value of acceleration \n");
	scanf("%d",&a);
	printf("enter value of time taken \n");
	scanf("%d",&t);
	
	v=u+a*t;
	
	printf("\nvalue of final velocity=%d",v);
	
	return 0;
}
