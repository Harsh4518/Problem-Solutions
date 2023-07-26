#include<stdio.h>

int main()
{
	int i,N,T1=0,T2=1,NT=0;
	
	printf("Enter Required Number\n");
	scanf("%d",&N);
	
	printf("\nSum of Fibonacci Series Upto %d Terms: %d %d ",N,T1,T2);
	
	NT=T1+T2;
	
	for(i=2;i<=N;i++)
	{
		
		printf("%d ",NT);
		T1=T2;
		T2=NT;
		NT=T1+T2;
		
	}
	
	return 0;

}
