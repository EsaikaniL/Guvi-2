#include <stdio.h>

int main()
{
   int a,k;
   float ans;
   printf("Enter the number:");
   scanf("%d",&a);
printf("\nEnter the K value:");
   scanf("%d",&k);
ans=a>>k;
printf("%.2f",ans);

    return 0;
}
