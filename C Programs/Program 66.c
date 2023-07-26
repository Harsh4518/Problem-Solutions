#include<stdio.h>

int Lsearch(int arr[],int n,int item)
{
	int i;
	
	for(i=0;i<n;i++)
	{
		if(arr[i]==item)
		
		 return i;
		 
	}
}

int main()
{
	int n,i,item,index=0;
	
	printf("Enter size of array:\n");
	scanf("%d",&n);
	
	int arr[n];
	
	printf("Enter elements in an array:\n");
	
	for(i=0;i<n;i++)
	
	 scanf("%d",&arr[i]);
	 
	printf("Enter element you to find:\n");
	
	scanf("%d",&item);
	
	index=Lsearch(arr,n,item);
	
	printf("\nElement exist at index no.: %d ",index);
	
	return 0; 
}
