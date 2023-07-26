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
	
	if(Per>=90.0 && Per<=100.0)
	 
	 printf("\nA Grade!");

else
    
	if(Per>=80.0 && Per<=90.0)
	 
	 printf("\nB Grade!");
	 
else
	
	if(Per>=60.0 && Per<=80.0)
	
	 printf("\nC Grade!");
	 
else
	
	 printf("\nD Grade!");
	 
	 printf("\n\n\n***Best of Luck!***");
	 
	
	return 0;  

}
