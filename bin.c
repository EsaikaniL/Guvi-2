#include<stdio.h>
void main()
{
	int a[100];
	int b[100];
	int c[100];
	int i,d,j,t,m;
	int rem=0,bin=0,base=1;
       int n;
       printf("How many number u want to insert \n");
      scanf("%d",&n);
       printf("Enter the numbers");
       for(i=0;i<n;i++)
      {
       scanf("%d",&a[i]);
      }
	for(i=0;i<n;i++)
	{
		b[i]=a[i];
 
	}
	for(i=0;i<n;i++)
	{
		d=0;
	 while(a[i]>0)
	 {
   	 rem=a[i]%2;
   	 if(rem==1)
   	 	d=d+1;
   	 bin=bin+rem*base;
   	 a[i]=a[i]/2;
   	 base=base*10;
	 }
	  c[i]=d;
	}
		printf("The number based on their binary 1's:\n");
		for(i=0;i<2;i++)
	{
		printf("%d's 1's is:%d",b[i],c[i]);
	}
	for(i=0;i<n;i++)
	{
		for(j=i+1;j<2;j++)
		{
			if(c[i]<c[j])
			{
				t=b[i];
				b[i]=b[j];
				b[j]=t;
				m=c[i];
				c[i]=c[j];
				c[j]=m;
			}
		}
	}
 
printf("The ans is:\n");
for(i=0;i<n;i++)
{
	printf("%d \n",b[i]);
}
 
}