#include<stdio.h>

int main()
{
	int N,i,j;
	char x;
	
	printf("Enter Value of N:\n");
	scanf("%d",&N);
	
	for(i=1;i<=N;i++)
	{
		x='A';
		
		for(j=1;j<=i;j++)
		{
			printf("%c",x++);
		}
		
		printf("\n");
	}
	
	return 0;
}
