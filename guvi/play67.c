#include <stdio.h>

int main(void) {
	int n,ans=1,i;
printf("Enter the number");
scanf("%d",&n);
for(i=1;i<n+1;i++)
{
ans=ans*i;
}
printf("\n%d",ans);
	return 0;
}
