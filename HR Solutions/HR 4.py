arr=[1,2,3]
sub_arr=[]
 
while len(arr)>0:

        c=0
        temp=min(arr)
        for i in range(len(arr)):
                arr[i]=arr[i]-temp
                c=c+1

        sub_arr.append(c)        
                
        arr.remove(min(arr))
        len(arr)-1

print(arr,sub_arr,len(arr))        
