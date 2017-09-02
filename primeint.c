#include<stdio.h>
void main()
{
int a,b,i,j,c=0;
printf("Enter the intervals");
scanf("%d%d",&a,&b);
printf("The prime number is:\n");
for(i=a;i<=b;i++)
{
c=0;
for(j=a;j<=(i/2);j++)
{
if(i%j==0)
c=1;
}
if(c==0&&i!=1&&i!=2)
printf("%d \n",i);
}
}