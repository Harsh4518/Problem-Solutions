#include<stdio.h>
#include<math.h>

int Sum(int,int);
int Subtract(int,int);

int main()
{
	int a,b,SUM,SUBTRACT;
	printf("Enter First Number\n");
	scanf("%d",&a);
	printf("Enter Second Number\n");
	scanf("%d",&b);
	
	SUM=Sum(a,b);
	SUBTRACT=Subtract(a,b);
	
	printf("\nSum of Numbers %d and %d is: %d",a,b,SUM);
	printf("\nsubtraction of Numbers %d and %d is: %d",a,b,SUBTRACT);
	
	return 0;

}

int Sum(int A,int B)
{
	int S1=0;
	
	S1=A+B;
	
	return S1;
}

int Subtract(int C,int D)
{
	
	int S2=0;
	
	S2=abs(C-D);
	
	return S2;
}
