#include<stdio.h>

void insert(int a[],int n,int pos,int key)
{
	int i;
	
	for(i=n-1;i>=pos-1;i--)
	{
		a[i+1]=a[i];
	}
	
	a[pos-1]=key;
	
	n++;
	
	printf("\nArray after insertion:\n");
	
	for(i=0;i<n;i++)
	 
	 printf("%d ",a[i]);
	
}

int main()
{
	int n,i,pos,key;
	
	printf("Enter the size of the array:\n");
	
	scanf("%d",&n);
	
	int a[n];
	
	printf("Enter the elements of the array:\n");
	
	for(i=0;i<n;i++)
	 
	 scanf("%d",&a[i]);
	 
	 printf("Enter the position at which element is going to inserted:\n");
	 
	 scanf("%d",&pos);
	 
	 printf("Enter the element you want to insert:\n");
	 
	 scanf("%d",&key);
	 
	 insert(a,n,pos,key);
	 
	 return 0;
}
