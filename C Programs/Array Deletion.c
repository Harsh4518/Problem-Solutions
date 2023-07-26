#include<stdio.h>

void delete(int a[],int n,int pos)
{
	int i;
	
	for(i=pos-1;i<n-1;i++)
	{
		a[i]=a[i+1];
	}
	
	n--;
	
	printf("\nArray after deletion of element:\n");
	
	for(i=0;i<n;i++)
	 
	 printf("%d ",a[i]);
	
}

int main()
{
	int n,i,pos;
	
	printf("Enter size of the array:\n");
	
	scanf("%d",&n);
	
	int a[n];
	
	printf("Enter elements of array:\n");
	
	for(i=0;i<n;i++)
	 
	 scanf("%d",&a[i]);
	 
	 
	 printf("Enter the position from where you want to delete element:\n");
	 
	 scanf("%d",&pos);
	 
	 delete(a,n,pos);
	 
	 return 0;
	
}
