#include<stdio.h>

int Palindrome(int);

int main()
{
	int Num,Result;
	
	printf("Enter Any Number\n");
	scanf("%d",&Num);
	
	Result=Palindrome(Num);
	
	if(Result==1)
	
	 printf("\nEntered Number %d is a Palindrome Number!\n",Num);
	 
	else
	 
	 printf("\nEntered Number %d is not a Palindrome Number!\n",Num);
	 
	return 0; 
}

int Palindrome(int X)
{
	int i,d,New=0,temp=0,count=0;
	
	temp=X;
	
	while(X!=0)
	{
		d=X%10;
		New=New*10+d;
		X=X/10;
	}
	
	if(New==temp)
	 
	 count++;
	 
	else
	 
	 count=0;
	
	return count;   
}
