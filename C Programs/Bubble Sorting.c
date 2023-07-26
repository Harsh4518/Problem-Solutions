/*BUBBLE SORTING*/


#include<stdio.h>

void BubbleSort(int a[],int n)
{
	int i,j,temp;
	
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(a[j]<a[i])
			{
				temp=a[i];
				
				a[i]=a[j];
				
				a[j]=temp;
			}
		}
	}
	
	printf("\nArray after Sorting:\n");
	 
	 for(i=0;i<n;i++)
	  
	  printf("%d ",a[i]);
	
}

int main()
{
	int n,i;
	
	printf("Enter the size of array:\n");
	
	scanf("%d",&n);
	
	int a[n];
	
	printf("Enter the elements of array:\n");
	
	for(i=0;i<n;i++)
	 
	 scanf("%d",&a[i]);
	 
	BubbleSort(a,n);
	
	return 0; 
}
