#include<stdio.h>
#include<ctype.h>
main()
{
	char c;
	printf("Enter a character \n");
	scanf("%c",&c);
	
	if(isupper(c))
	  c=tolower(c);
	else
	  c=toupper(c);
	  
	printf("\nupdated character=%c",c);
	
	return 0;  
	
	
}
