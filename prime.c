#include<stdio.h>
void main()
{
int a,i,c=0;
printf("Enter the number");
scanf("%d",&a);
for(i=2;i<=(a/2);i++)
{
if(a%i==0||a==2)
c=1;
}
if(c==0)
printf("Prime");
else
prinf("Not prime");
}
