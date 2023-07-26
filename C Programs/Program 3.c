#include<stdio.h>
int main()
{
	float F,C;
	printf("enter temperature in fahrenhiet \n");
	scanf("%f",&F);
	
	C=(F-32)*5/9;
	
	printf("\n Temperature in  Celcius=%f",C);
	
	return 0;
}
