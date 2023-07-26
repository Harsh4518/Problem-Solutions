#include<stdio.h>
#include<math.h>

int main()
{
	int a,b,Temp=0,count=0,i,d,Sum=0;
	
	printf("Enter First Range\n");
	scanf("%d",&a);
	printf("Enter Second Range\n");
	scanf("%d",&b);
	
	printf("\nArmstrong Number Between %d And %d are as follows: ",a,b);
	
	for(i=a;i<=b;i++)
	{
		
		Temp=i;
	
	    while(Temp!=0)
	   {
	   	
	   	Temp=Temp/10;
	   	count++;
	 	
       }
	   
	   Temp=i;
	   
	   while(Temp!=0)
	   {
	   	
	   	d=Temp%10;
	   	Sum=Sum+pow(d,count);
	   	Temp=Temp/10;
	   	
	   }
	   
	   if(Sum==i)
	    
		printf("%d ",Sum);	
		
	   Sum=0;
	   count=0;
		
	}
	
	return 0;

}

