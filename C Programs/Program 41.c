#include<stdio.h>

void Swap(int*,int*);

int main()
{
	int a,b;
	
	printf("Enter First Number!\n");
	scanf("%d",&a);
	printf("Enter Second Number!\n");
	scanf("%d",&b);
	
	printf("\nNumber Before Swapping: %d%d",a,b);
	
	Swap(&a,&b);
	
	printf("\nNumber After Swapping: %d%d",a,b);
	
	return 0;
}

void Swap(int*X,int*Y)
{
	int temp;
	 
    temp=*X;
    *X=*Y;
    *Y=temp;
}
