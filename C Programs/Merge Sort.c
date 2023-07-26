#include<stdio.h>

void Merge(int a[],int beg,int mid,int end)
{
	int i,j,k,b[10];
	
	i=beg;
	j=mid+1;
	k=beg;
	
	while(i<=mid && j<=end)
	{
		if(a[i]<a[j])
		{
			b[k]=a[i];
			i++;
		}
		else
		{
			b[k]=a[j];
			j++;
		}
		
		k++;
	}
	
	if(i>mid)
	{
		while(j<=end)
		{
			b[k]=a[j];
			k++;
			j++;
		}
	}
	
	else
	{
		while(i<=mid)
		{
			b[k]=a[i];
			k++;
			i++;
		}
	}

}

void MergeSort(int a[],int beg,int end)
{
	int mid;
	
	if(beg<end)
	{
		mid=(beg+end)/2;
		MergeSort(a,beg,mid);
		MergeSort(a,mid+1,end);
		Merge(a,beg,mid,end);
	}
	
}

int main()
{
	int n,i,beg,end;
	
	printf("Enter the Size of Array:\n");
	scanf("%d",&n);
	
	int a[n];
	
	printf("\nEnter the elements of array:\n");
	
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	
	beg=0;
	end=n-1;
	
	printf("\nArray Before Sorting:\n\n");
	
	for(i=0;i<n;i++)
	printf("%d ",a[i]);
	
	MergeSort(a,beg,end);

	return 0;
}
