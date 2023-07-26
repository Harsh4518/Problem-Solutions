#include<stdio.h>
main()
{
	float BS,HRA,GS,DA;
	printf("enter value of base salary\n");
	scanf("%f",&BS);
	
	DA=0.2*BS;
	HRA=2.5*BS;
	GS=BS+DA+HRA;
	
	printf("\ngross salary of a person=%.1f",GS);
	
	return 0;
	
}
