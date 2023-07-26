*****BUBBLE SORT*****

/* void Bubble_Sort(int a[],int n) 
{
	int i,j,temp;
	
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<n;j++)
		{
			if(a[i]>a[j])
			{
				temp=a[j];
				a[j]=a[i];
				a[i]=temp;
			}
		}
		
	}
} */

*************************

*****SELECTION SORT*****

/* void Selection_Sort(int a[],int n)
{
	int i,j,min;
	
	for(i=0;i<n-1;i++)
	{
		min=i;
		
		 for(j=i+1;j<i;j++)
		 {
		 	if(a[min]>a[j])
		 	
		 	   min=j;
		 }
		 
		 temp=a[min];
		 a[min]=a[i];
		 a[i]=temp; 
	
	}

} */

*************************

*****INSERTION SORT*****

/* void Insertion_Sort(int a[],int n)
{
	int i,j,min;
	
	for(i=1;i<n;i++)
	{
		min=a[i];
		
		j=i-1;
		
		while(j>=0 && a[j]>min)
		{
			a[j+1]=a[j];
			
			j=j-1;
		}
		
		a[j+1]=min;
	}
} */

*************************


*****MERGE SORTING*****

/* void MergeSort(int a[],int beg,int end)
{
	int mid;
	
	if(beg<end)
	{
		mid=(beg+end)/2;
		
		MergeSort(a,beg,mid);
		MergeSort(a,mid+1,end);
		Merge(a,beg,mid,end);
		
	}
}

void Merge(int a,int beg,int mid,int end)
{
	int i,j,k,b[20];
	
	i=beg;
	j=end+1;
	k=beg;
	
	while(i<=beg && j<=end)
	{
		if(a[i]<a[j])
		{
			b[k]=a[i];
			i++;
		}
		else
		{
			b[k]=a[j];
			j++;
		}
		
	  k++;
	}
	
	if(i>mid)
	{
		while(j<=end)
		{
			b[k]=a[j];
			k++;
			j++;
		}
	}
	else
	{
		while(i<=mid)
		{
			b[k]=a[i];
			k++;
			i++;
		}
	}
} /*

*************************
