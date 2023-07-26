#include<stdio.h>

int main()
{
	int N,Element,i,Loc;
	
	printf("Enter The Size of Array:\n");
	scanf("%d",&N);
	
	int Arr[N];
	
	printf("Enter Elements of Array:\n");
	
	for(i=0;i<N;i++)
	{
		scanf("%d",&Arr[i]);
	}
	
	printf("Enter Element You Want to Search For:\n");
	scanf("%d",&Element);
	
	for(i=0;i<N;i++)
	{
		if(Arr[i]==Element)
		 
		 Loc=i;
	}
	
	printf("So! Element %d is At index Number: %d",Element,Loc);
	printf("\nAddress of Element %d is: %d",Element,&Arr[Loc]);
	printf("\nPosition of Element %d is: %d",Element,Loc+1);
	
	return 0;
}
