#include<stdio.h>
int main()
{
	int num,d,rev=0,temp;
	
	printf("Enter Any Number:\n");
	scanf("%d",&num);
	
	temp=num;
	
	while(num!=0)
	{
		d=num%10;
		rev=rev*10+d;
		num=num/10;
	}
	
	(rev==temp)?printf("\nEntered Number %d is a Palindrome Number!",temp):printf("\nEntered Number %d is not a palindrome Number!",temp);


    return 0;

}


