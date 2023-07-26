#include<stdio.h>

int main()
{
	int a[4][5]={{0,0,0,2,5},{0,0,5,2,5},{1,0,0,0,2},{1,3,0,0,0}};
	
	int m=4,n=5;
	
	int c[10][10],i,j,h=0,k=0;
	
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			if(a[i][j]!=0)
			{
				c[h][k]=i;
				h++;
				c[h][k]=j;
				h++;
				c[h][k]=a[i][j];
     			k++;
     			h=0;
     		}
		}
	}
	
	for(i=0;i<3;i++)
	{
		for(j=0;j<6;j++)
		{
			printf("%d ",c[i][j]);
		}
		
		printf("\n");
	}
	
	return 0;
}
