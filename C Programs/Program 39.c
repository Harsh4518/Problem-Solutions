#include<stdio.h>

int Prime(int);

int main()
{
	int Num,Result;
	
	printf("Enter Any Number\n");
	scanf("%d",&Num);
	
	Result=Prime(Num);
	
	if(Result==1)
	
	 printf("\nEntered Number %d is A Prime Number!\n",Num);
	
	else
	
	 printf("\nEntered Number %d is Not A Prime Number!\n",Num);
	 
	return 0; 
	
}

int Prime(int A)
{
	int i,count=0;
	
	for(i=1;i<=A/2;i++)
	{
		if(A%i==0)
		count++;
	}
	
	return count;
}
