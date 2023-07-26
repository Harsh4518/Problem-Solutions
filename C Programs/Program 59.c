#include<stdio.h>

int main()
{
	int N,i,Sum=0;
	
	float Avg=0;
	
	printf("Enter Size of Array:\n");
	scanf("%d",&N);
	
	int Arr[N];
	
	printf("Enter %d Elements of Array:\n",N);
	
	for(i=0;i<N;i++)
	{
		scanf("%d",&Arr[i]);
		Sum=Sum+Arr[i];
	}
	
	Avg=(float)Sum/N;
	
	printf("\nAverage of Elements Present in Array: %.2f\n",Avg);
	
	return 0;
	
}
