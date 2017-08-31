#include<stdio.h>
void main()
{
int i,n,sum=0;
printf("Enter n value");
scanf("%d",&n);
if(n>0)
{
 for(i=1;i<=n;i++)
 {
 sum=sum+i;
 }
printf("The sum of %d nat number is:%d",n,sum);
}
else
printf("n value is not natural");
}
