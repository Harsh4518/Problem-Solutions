#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{ 
    int M,i,flag=0,pos,n;
    
    scanf("%d",&n);
    
    int arr[n];
    
    if(n>0 && n<1010)
    {    
    
        for(i=1;i<=n;i++)
       
        scanf("%d",&arr[i]);
    }
    
    scanf("%d",&M);
    
    
    if(M>0 && M<100001)
    {

         for(i=1;i<=n;i++)
         {
             if(arr[i]==M)
             {
                 flag=1;
                 pos=i;
             }   
         }
        
        if(flag==1)
             
            printf("%d",pos);
        
        else
            
           if(flag!=1)
             
            printf("-1");
        
    }   

 
    return 0;
} 
