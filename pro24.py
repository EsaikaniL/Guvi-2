#include<stdio.h>
void main()
{
	int k;
	int i,num=1,rem,base,bin,b;
	printf("\n");
	printf("Enter k value: \n");
	scanf("%d",&k);
	for(i=0;i<k;i++)
	{
		num=num*2;
	}
	printf("The %d digit binary values:\n",k);
	for(i=0;i<num;i++)
	{
		b=i;
		rem=0,base=1,bin=0;
		while(b!=0)
		{
			rem=b%2;
			bin=bin+rem*base;
			base=base*10;
			b=b/2;
		}
		printf("%d \n",bin);
	}
}
© 2018 GitHub, Inc.
