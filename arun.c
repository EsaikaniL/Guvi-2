#include<stdio.h>
void main()
{
char c;
printf("Enter the character");
scanf("%c",c);
if(c>='a'&&c<='z'||c>='A'&&c<='Z')
printf("Alphabet");
else
printf("Not alphabet");
}
