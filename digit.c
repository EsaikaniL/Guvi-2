#include<stdio.h>
void main()
{
int n,c=0;
printf("Enter any number");
scanf("%d",&n);
while(n!=0)
{
n=n/10;
c++;
}
printf("The digit of %d is:%d",n,c);
}
