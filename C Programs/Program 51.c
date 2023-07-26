#include<stdio.h>

int main()
{
	int N,i,sum=0,Max,Loc;
	
	printf("Enter Size of Array:\n");
	scanf("%d",&N);
	
	int Arr[N];
	
	printf("Enter %d Elements in an array:\n",N);
	
	for(i=0;i<N;i++)
	{
		scanf("%d",&Arr[i]);
	}
	
	Max=Arr[0];
	Loc=0;
	
	for(i=0;i<N;i++)
	{
		if(Arr[i]>Max)
		{
			Max=Arr[i];
			Loc=i;
		}
	}
	
	printf("\nMaximum Value in the Array: %d\n",Max);
	printf("Location of Max Value in the Array: %d\n",Loc);
	printf("Adress of Maximum Value the Array: %u\n",&Arr[Loc]);
	printf("Position of Maximum Value in the Array: %d\n",Loc+1);
	
	return 0;

}
