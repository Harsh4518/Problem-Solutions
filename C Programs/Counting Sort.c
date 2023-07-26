#include<stdio.h>

void Counting_sort(int a[],int n)
{
	int f[n],result[n],max,i;
	
	max=a[0];
	
	for(i=1;i<n;i++)
	{
		if(a[i]>max)
		{
			max=a[i];
		}
	}
	
	for(i=0;i<n;i++)
	{
		f[i]=0;
	}
	
	for(i=0;i<n;i++)
	{
		f[a[i]]++;
	}
	
	for(i=1;i<=max;i++)
	{
		f[i]=f[i]+f[i-1];
	}
	
	for(i=n-1;i>=0;i--)
	{
     	result[f[a[i]]-1]=a[i];
     	f[a[i]]--;
    }
    
    for(i=0;i<n;i++)
    {
    	a[i]=result[i];
	}
	
}

int main()
{
	int n,i;
	
	printf("Enter the size of array:\n");
	scanf("%d",&n);
	
	int a[n];
	
	printf("\nEnter the elements of array:\n");
	
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	
	printf("\nArray before sorting:\n");
	
	for(i=0;i<n;i++)
    printf("%d ",a[i]);
    
    Counting_sort(a,n);
    
    printf("\n\nArray After sorting is:\n");
    
    for(i=0;i<n;i++)
    printf("%d ",a[i]);
    
    return 0;

}
