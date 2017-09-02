#include<stdio.h>
void main()
{
int a,b
printf("Enter the intervals");
scanf("%d%d",&a,&b);
for(i=a;i<=b;i++)
{
if(i%2==0)
continue;
else
printf("%d",i);
}
}