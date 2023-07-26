#include<stdio.h>

int main()
{
	int Arr[5],sum=0,i;
	
	printf("Enter 5 Elements in Array:\n");
	
	for(i=1;i<=5;i++)
	{
		scanf("%d",&Arr[i]);
	}
	
	for(i=1;i<=5;i++)
	{
		sum=sum+Arr[i];
	}
	
	printf("\nSum of 5 Elements in array: %d",sum);
	
	return 0;
	
}
