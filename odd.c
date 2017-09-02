#include<stdio.h>
void main()
{
int a,b,i;
printf("Enter the intervals");
scanf("%d%d",&a,&b);
  printf("The odd numbers are:");
for(i=a;i<=b;i++)
{
if(i%2==0)
continue;
else
printf("%d \n",i);
}
}
