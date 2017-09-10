#include<stdio.h>
void main()
{	
      int k;
      int a[10];
    int b[10],c[10],m=0,n=0;
	int i,p,q;
      printf("Enter the no of value \n");
      scanf("%d",&k);
     printf("Enter the elements \n");
     for(i=0;i<k;i++) 
    {
      scanf("%d",&a[i]);
    }
	for(i=0;i<k/2;i++)
	{
		b[i]=a[i];
	}
	for(i=k/2;i<k;i++)
	{
		c[i]=a[i];
	}
	for(i=0;i<k/2;i++)
	{
		m=m+b[i];
	}
	for(i=k/2;i<k;i++)
	{
		n=n+c[i];
	}
	p=(m/(k/2));
	q=(n/(k-(k/2)));
	if(p==q)
	{
		printf("The 1st part is:\n");
		for(i=0;i<k/2;i++)
		{
			printf("%d \t",b[i]);
		}
		printf("\n");
		printf("The 2nd part is:\n");
		for(i=k/2;i<k;i++)
		{
			printf("%d \t",c[i]);
		}
	}
	else
	printf("It is not possible to devide");
}