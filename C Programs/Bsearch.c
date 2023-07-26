#include<stdio.h>

int Bsearch(int a[],int n,int key)
{
	int beg=0,end=n-1,mid,i;
	
	mid=(beg+end)/2;
	
	for(i=0;i<n-1;i++)
	{
		if(a[mid]>key)
		  
		  end=mid-1;
		  
	else 
		 
		 if(a[mid]<key)
		  
		   beg=mid+1;
		
	else 
		 
		 return mid;    
		  
	}
	
}

int main()
{
	int n,i,key,pos;
	
	printf("Enter the size of the array:\n");
	
	scanf("%d",&n);
	
	int a[n];
	
	printf("Enter the elements of array:\n");
	
	for(i=0;i<n;i++)
	 scanf("%d",&a[i]);
	 
	 printf("Enter element you want to search:\n");
	 
	 scanf("%d",&key);
	 
	 pos=Bsearch(a,n,key);
	 
	 printf("Element found at index: %d \n",pos);
	 
	 return 0;
	 
}
