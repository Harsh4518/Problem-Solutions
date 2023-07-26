#include<stdio.h>
#include<math.h>
int main()
{
	int P,R,T;
	float PI,CI;
	printf("Enter value of Principle amount\n");
	scanf("%d",&P);
    printf("Enter value of Rate\n");
	scanf("%d",&R);
	printf("Enter value of Time\n");
	scanf("%d",&T);
	
	PI=(P*R*T)/100;
	CI=P*(pow((1+R/100),T))-P;
	
	printf("\nPrinciple Interest=%f",PI);
	printf("\nCompound Interest=%f",CI);
	
	return 0;
}
