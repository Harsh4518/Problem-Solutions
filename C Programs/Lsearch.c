#include<stdio.h>

int Lsearch(int a[],int n,int key)
{
	
	int i;
	
	for(i=0;i<n;i++)
	{
		if(a[i]==key)
		{
		 return i;
		 break;
        }
	}
	
	
}

int main()
{
	int n,i,key,index;
	
	printf("Enter no of Elements in the array:\n");
	
	scanf("%d",&n);
	
	int a[n];
	
	printf("\nEnter Elements of array:\n");
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	
	printf("Enter Key you want to find:\n");
	
	scanf("%d",&key);
	
	index=Lsearch(a,n,key);
	
	printf("\nElement found at index: %d",index);
	
	return 0;
}
