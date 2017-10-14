#include <stdio.h>
int main()
{
   char str[20];
   int i,j,k;
   gets(str);
   for(i=0;str[i]!='\0';i++);
   for(k=0;k<i;k++)
   {
   	printf("%c\t",str[k]);
   }
   printf("\n");
   for(j=0;j<i;j++)
   {
   	printf("%c",str[j]);
   	for(k=0;k<i-1;k++)
   	{
   		printf("\t");
   	}
   	printf("%c",str[j]);
   	printf("\n");
   }
    for(k=0;k<i;k++)
   {
   	printf("%c\t",str[k]);
   }
   return 0;
}
