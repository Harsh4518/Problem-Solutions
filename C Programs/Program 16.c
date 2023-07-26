#include<stdio.h>
main()
{
	int year;
	printf("enter value of year\n");
	scanf("%d",&year);
	
	if(year%4==0)
	   printf("Given year %d is a leap year",year);
	else
	   printf("Given year %d is not a leap year",year);
	   
	  return 0;
	  
}
	
	    
	

