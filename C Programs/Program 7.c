#include<stdio.h>
int main()
{
	int x1,x2,y1,y2;
	float c,m;
	
	printf("Enter value of X1\n");
	scanf("%d",&x1);
	printf("Enter value of Y1\n");
	scanf("%d",&y1);
	printf("Enter value of X2\n");
	scanf("%d",&x2);
	printf("Enter value of Y2\n");
	scanf("%d",&y2);
	
	m=(y2-y1)/(x2-x1);
	c=y1-(m*x1);
	
	printf("\n Equation of Line:Y=%.1fX+%.1f",m,c);
	
	return 0;
}
