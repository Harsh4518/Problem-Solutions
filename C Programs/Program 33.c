#include<stdio.h>
#include<math.h>

main()
{
	int i,N,SE=0,SO=0;
	
	printf("Enter The Last Number\n");
	scanf("%d",&N);
	
	for(i=1;i<=N;i++)
	{
		if(i%2==0)
        
		 SE+=i;
	
		else
		 
		 SO+=i;		
	}
	
	printf("\nSum of Even Numbers Between 1 And %d is: %d ",N,SE);
	printf("\nSum of Odd Numbers Between 1 And %d is: %d",N,SO);
	
	return 0;

}
