#include<stdio.h>
int main()
{
	int num,sum=0,i;
	
	printf("Enter any Number:");
	scanf("%d",&num);
	
	for(i=1;i<=num;i++)
	{
		sum=sum+i;
	}
	
	printf("\nSum of First %d natural Numbers= %d",num,sum);
	
	return 0;
	
}
