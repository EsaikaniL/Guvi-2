#include <stdio.h>
 int main(void) {
	int n,a,c=0,t;
	printf("Enter number\n");
	scanf("%d",&n);
	a=n;
	while(n>1)
	{
		t=n%2;
	   if (t==0)
	   {
	   	c=1;
	   }
	   else
	   {
	   	c=0;
	   }
	    n=n/2;
	}
if(c==0)
{
	printf("%d is not pow of 2",a);
}
else
{
	printf("%d is a pow of 2",a);
}
}
