#include <stdio.h>

int main(void) {
	int a[20],i,k,n;
printf("\nHow many elements??");
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
printf("\nHow many elements to delete??");
scanf("%d",&k);
for(i=0;i<n-k;i++)
{
printf("\n%d",a[i]);
}
	return 0;
}
