#include<stdio.h>

void insert(int *arr,int n,int E,int pos)
{
	int i;
	
	if(pos<0 && pos >n)
	
	 printf("Wrong Input!\n");
	 
    else
	 
	 {
	 	
	 	for(i=n-1;i>=pos-1;i--)
	 	{
	 		
	 		arr[i+1]=arr[i];
	 	}
	 	
	 	arr[pos-1]=E;
	 	
	} 

}

int main()
{
	int n,i,E,pos;
	
	printf("Enter Size of array\n");
	
	 scanf("%d",&n);
	 
	int arr[n];
	
	printf("Enter %d Elements in array:",n);
	
	for(i=0;i<n;i++)
	 
	 scanf("%d",&arr[i]);
	 
	printf("Enter the element you want to enter:");
	
	scanf("%d",&E);
	
	printf("\nEnter the position:");
	
	 scanf("%d",&pos);
	 
	 printf("\nArray Before insertion:\n");
	 
	 for(i=0;i<n;i++)
	 {
	 	printf("%d ",arr[i]);
	 }
	 
	 insert(arr,n,E,pos);
	 n++;
	 
	printf("\nArray after insertion of element:\n");
	
	for(i=0;i<n;i++)
	
	 printf("%d" ,arr[i]); 
	 
}
