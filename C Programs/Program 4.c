#include<stdio.h>
int main()
{
	int r;
	float C,A;
	printf("enter radius of circle\n");
	scanf("%d",&r);
	
	C=2*3.14*r;
	A=3.14*r*r;
	
	printf("\nArea of circle=%f",A);
	printf("\nCircumference of circle=%f",C);
	
	return 0;
}
