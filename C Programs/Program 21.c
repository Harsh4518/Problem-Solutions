#include<stdio.h>
int main()
{
	char ch;
	printf("enter any charcter:");
	scanf("%c",&ch);
	
	if( (ch>='a' && ch<='z') || (ch>='A' && ch<='Z') )
	{
	
	   if(ch=='a'|| ch=='A' || ch=='e' || ch=='E' || ch=='i' || ch=='I' || ch=='o' || ch=='O' || ch=='u' || ch=='U')
	 
	      printf("\nEntered character is a vowel");
	
       else
       
          printf("\nEntered character is a consonent");
    }
    
    else
    
        printf("\nEntered character is a special symbol or a number!");
		
	
	return 0;
	
}
