#include<stdio.h>
main()
{
	char c;
	printf("enter a character \n");
	scanf("%c",&c);
	
	if(c>='A'&& c<='Z')
	  c=c+32;
	else
	  c=c-32;
	  
	printf("\n Updated Character=%c",c);
	
	return 0;  
}
