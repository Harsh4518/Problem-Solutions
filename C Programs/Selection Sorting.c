#include<stdio.h>

void SELECTION_SORT(int a[],int n)
{
	
	int i,j,min;
	
	for(i=0;i<n-1;i++)
	{
		min=i;
		
		for(j=i+1;j<n;j++)
		{
			if(a[j]<a[min])
			
			 	min=j;
		
        }
		
	    int temp=a[min];
		
		a[min]=a[i];
		
 		a[i]=temp;
		
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
	 
	 SELECTION_SORT(a,n);
	 
	 return 0;
	 
	 
}
