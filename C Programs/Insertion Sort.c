#include<stdio.h>

void Insertion_Sort(int a[],int n)
{
	
	int i,j,min;
	
	for(i=1;i<n;i++)
	{
		min=a[i];
		
		j=i-1;
		
		while(j>=0 && a[j]>min)
		{
			a[j+1]=a[j];
			
			j=j-1;
		}
		
		a[j+1]=min;
	}
	
	return;
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
	 
	Insertion_Sort(a,n);
	
	printf("\nArray after Sorting:\n");
	
	for(i=0;i<n;i++)
	 
	 printf("%d ",a[i]);
	 
	 return 0;
}
