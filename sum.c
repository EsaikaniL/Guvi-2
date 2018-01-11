#include <stdio.h>
 
int main(void) {
	int i,sum=0,n,k,a[30];
printf("Enter N value");
scanf("%d",&n);
printf("Enter K value");
scanf("%d",&k);
printf("Enter tha array values");
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<k;i++)
{
  sum=sum+a[i];
}
printf("The sum is %d:",sum);
	return 0;
}
