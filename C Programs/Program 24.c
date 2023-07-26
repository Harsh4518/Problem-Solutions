#include<stdio.h>
#include<math.h>

int main()
{
	int a,b;
	char ch;
    
	printf("\t\t\t\t****WELCOME TO BASIC CALCULATOR****\n"); 
	printf("Enter first Number:\n");
	scanf("%d",&a); 
    printf("Enter Second Number:\n");
	scanf("%d",&b);
	fflush(stdin);
	printf("Enter An Operator---->\n + \n - \n * \n / \nEnter Your Choice!\n");
	scanf("%c",&ch);
	
	
	switch(ch)
	{
		case'+':
		
		printf("\nSum of Two Numbers %d and %d = %d",a,b,(a+b));
		break;
		
		case'-':
		
		printf("\nDifference of Two Numbers %d and %d = %d",a,b,abs(a-b));
		break;
		
	    case'*':
		
		printf("\nProduct of Two Numbers %d and %d = %d",a,b,(a*b));
		break;
		
		case'/':
		
		printf("\nDivision of Two Numbers %d and %d = %d",a,b,(a/b));
		break;
		
		default:
		
		printf("\n\n\n\t\t\t\t****Please Enter Appropriate Value!****\n");	
		
	}
	
	printf("\n\n\n\t\t\t\t****THANK YOU! HAVE A NICE DAY!****");
	
	return 0;
}

