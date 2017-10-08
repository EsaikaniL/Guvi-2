#include<stdio.h>
void main()
{
char d;
printf("Enter the character");
scanf("%c",d);
if(d>='a'&&d<='z'||d>='A'&&d<='Z')
printf("Alphabet");
else
printf("Not alphabet");
}
