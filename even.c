#include<stdio.h>
void main()
{
int a,b,i;
printf("Enter the intervals");
scanf("%d%d",&a,&b);
printf("The even number is:");
for(i=a;i<=b;i++)
{
if(i%2==0)
printf("%d \n",i);
else
continue;
}
}