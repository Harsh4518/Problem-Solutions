#include<stdio.h>

int main()
{
	int N,i,Pos;
	
	printf("Enter Size of Array:\n");
	scanf("%d",&N);
	
	int Arr[N];
	
	printf("\nEnter %d Elements in the Array:\n",N);
	
	for(i=0;i<N;i++)
	{
		scanf("%d",&Arr[i]);
	}
	
	printf("\nArray Before Deletion:\n");
	
	for(i=0;i<N;i++)
	{
		printf("%d ",Arr[i]);
	}
	
	printf("\n\nEnter Position of Element to Be Deleted:\n");
	scanf("%d",&Pos);
	
	if(Pos>N-1)
	
	 printf("\nDELETION NOT POSSIBLE!...");
	 
	else
	 
	{
	  	for(i=Pos-1;i<N-1;i++)
	  	{
	  		Arr[i]=Arr[i+1];
		}
		
		N--;
		
		printf("\nArray After Deletion:\n");
		
		for(i=0;i<N;i++)
		{
			printf("%d ",Arr[i]);
		}
	  	
	}
	
	return 0; 
}
