#include<stdio.h>
void main()
{
int a,b,n,i;
printf("Enter the number");
scanf("%d",&a);
b=a;
printf("Enter the power");
scanf("%d",&p);
for(i=1;i<=n-1;i++)
{
a=a*a;
}
printf("The %d power of %d is:%d",n,b,a);
}
