#include<stdio.h>
void main()
{
int a,n,r,b=0;
printf("Enter the number");
scanf("%d",&a);
r=a;
while(a!=0)
{
n=a%10;
b=(b*10)+n;
a=a/10;
}
if(r==b)
printf("The given number %d is palindrome",r);
else
printf("The given number %d is not palindrome",r);
}
