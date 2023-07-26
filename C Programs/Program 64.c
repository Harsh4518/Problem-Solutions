#include<stdio.h>

int Bsearch(int a[],int n,int key)
{
	
	int mid,l=0,h=n-1,i;
	
	mid=(l+h)/2;
	
	for(i=0;i<n-1;i++)
	{
		if(h<l)
		
		 return 0;
		 
		else 
		
		 if(a[mid]>key)
		  
		   h=mid-1;
		
		else 
		 
		 if(a[mid]<key) 
		  
		  l=mid+1;
		 
		else
		 
		 return mid;     
	}
	
}

int main()
{
	int n,i,key,result;
	
	printf("Enter size of array:\n");
	
	scanf("%d",&n);
	
	int a[n];
	
	printf("enter elements of array:\n");
	
	for(i=0;i<n;i++)
	
	scanf("%d",&a[i]);
	
	printf("Enter the element you want to search:\n");
	
	scanf("%d",&key);
	
	result=Bsearch(a,n,key);
	
	printf("\nElement found at index No.: %d",result);
	
	return 0;

}
