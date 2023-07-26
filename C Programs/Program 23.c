#include<stdio.h>
int main()
{
	int M,C,SS,Ch,Ec;
	float Per;
	
	printf("enter marks of Maths:\n");
	scanf("%d",&M);
	printf("enter marks of C language:\n");
	scanf("%d",&C);
	printf("enter marks of Soft Skills:\n");
	scanf("%d",&SS);
	printf("enter marks of Chemistry:\n");
	scanf("%d",&Ch);
	printf("enter marks of Electrical:\n");
	scanf("%d",&Ec);
	
	Per=(M+C+SS+Ch+Ec)*100/500;
	
	if(Per>=75.0 && Per<=100.0)
	 
	 printf("\nFirst division Passout!");

else
    
	if(Per>=60.0 && Per<=74.0)
	 
	 printf("\nSecond division Passout!");
	 
else
	
	if(Per>=33.0 && Per<=59.0)
	
	 printf("Third division Passout!\n");
	 
else
	
	 printf("***You are Failed!***");
	 
	 printf("\n***Best of Luck!***");
	 
	
	return 0;  

}
