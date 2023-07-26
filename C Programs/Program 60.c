#include<stdio.h>

int main()
{
	int N,i,Element,Pos;
	
	printf("Enter Size of Array:\n");
	scanf("%d",&N);
	
	int Arr[N];
	
	printf("\nEnter %d Elements in the Array:\n");
	
	for(i=0;i<N;i++)
	{
		scanf("%d",&Arr[i]);
	}
	
	printf("\nEnter Element to be Inserted:\n");
	scanf("%d",&Element);
	
	printf("\nEnter Position Where Element %d is to Inserted:\n",Element);
	scanf("%d",&Pos);
	
	printf("\nArray Before Insertion:\n\n");
	
	for(i=0;i<N;i++)
	{
		printf("%d ",Arr[i]);
	}
	
	
	for(i=N-1;i>=Pos-1;i--)
	{
		Arr[i+1]=Arr[i];
	}
	
	Arr[Pos-1]=Element;
	
	N++;
	
	printf("\n\nArray After Insertion Element %d is:\n\n",Element);
	
	for(i=0;i<N;i++)
	{
		printf("%d ",Arr[i]); 
	}
	
	return 0;
}
