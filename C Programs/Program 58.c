#include<stdio.h>

int main()
{
	int N,i,Max,count=0;
	
	printf("Enter Size of Array:\n");
	scanf("%d",&N);
	
	int Arr[N];
	
	printf("Enter Elements of An Array:\n");
	
	for(i=0;i<N;i++)
	{
		scanf("%d",&Arr[i]);
	}
	
	Max=Arr[0];
	
	for(i=0;i<N;i++)
	{
		if(Arr[i]>Max)
		 
		 Max=Arr[i];
	}
	
	for(i=0;i<N;i++)
	{
		if(Arr[i]==Max)
		 
		 count++;
	}
	
	printf("\nMaximum No in the Array is: %d",Max);
	
	printf("\nTotal Occurence of Maximum Number %d is: %d",Max,count);
	
	return 0;
}
