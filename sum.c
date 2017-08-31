#include<stdio.h>
void main()
{
int i,sum=0,n;
printf("Enter any pos number");
scanf("%d",&n);
for(i=1;i<=n;i++)
{
sum=sum+i;
}
printf("The sum of %d is %d:",n,sum);
}
