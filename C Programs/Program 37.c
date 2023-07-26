#include<stdio.h>

int main()
{
	int i,Num,fact=1;
	
	printf("Enter Any Number:\n");
	scanf("%d",&Num);
	
	for(i=1;i<=Num;i++)
	
	 {
	  fact=fact*i;
	 }
	
	printf("\nFactorial of Given Number %d is: %d",Num,fact);
	
    return 0;
	 
}
