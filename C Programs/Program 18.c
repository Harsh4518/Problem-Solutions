#include<stdio.h>
main()
{
	int a,b,c;
	
	printf("enter first number\n");
	scanf("%d",&a);
    printf("enter second number\n");
	scanf("%d",&b);
	printf("enter third number\n");
	scanf("%d",&c);
	
	if(a>b&&a>c)
	 
	 printf("\nGreatest number between %d %d %d is %d",a,b,c,a);
	 
	 else
	
	if(b>a&&b>c)
 
 	 printf("\nGreatest number between %d %d %d is %d",a,b,c,b);
	
	 else
	 
	 printf("\nGreatest number between %d %d %d is %d",a,b,c,c);
	 
	 return 0;
	

}
