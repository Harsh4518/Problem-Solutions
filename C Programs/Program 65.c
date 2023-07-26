#include<stdio.h>

void delete(int a[],int n,int pos)
{
	int i;
	
	for(i=pos-1;i<n-1;i++)
	{
		a[i]=a[i+1];
	}
	
}

int main()
{
	int n,i,pos;
	
	printf("Enter size of Array:\n");
	
	scanf("%d",&n);
	
	int a[n];
	
	printf("Enter elements of array:\n");
	
	for(i=0;i<n;i++)
	 
	 scanf("%d",&a[i]);
	
    printf("Enter position of element to be deleted:\n");
    
    scanf("%d",&pos);
	
	printf("Array before deletion:\n");
	
	for(i=0;i<n;i++)
	 
	 printf("%d ",a[i]);
	 
	printf("\n\nyou to want to delete element from position: %d\n",pos);
	
	
	delete(a,n,pos);
	n--;
	
	printf("\nArray after deletion:\n");
	
	for(i=0;i<n;i++)
	
	printf("%d ",a[i]);
	
	 return 0;
	 
}
