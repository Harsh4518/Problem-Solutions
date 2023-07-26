#include<stdio.h>
#include<math.h>
main()
{
	int a,b,c;
	float r1,r2,d;
	
	printf("enter value of a \n");
	scanf("%d",&a);
	printf("enter value of b \n");
	scanf("%d",&b);
    printf("enter value of c \n");
	scanf("%d",&c);
	
	d=b*b-4*a*c;

	r1=(-b+sqrt(d))/2*a;
	r2=(-b-sqrt(d))/2*a;
	
    if(d<0)
     
	 printf("\nRoots of Quadratic Equation are Imaginary!");
    
    else
    
	 printf("\nRoots of Quadrtic are %.1f and %.1f.",r1,r2);
	 
	 return 0;
	
}

