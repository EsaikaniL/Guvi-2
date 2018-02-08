#include <stdio.h>

int main(void) {
	int a[20],n,i,k;
printf("How many elements??\n");
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("Enter the K value\n");
scanf("%d",&k);
for(i=0;i<n;i++)
{
if(a[i]<=k)
{
printf("%d\n",a[i]);
}
}
	return 0;
}
