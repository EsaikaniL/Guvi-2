#include <stdio.h>
#include<math.h>
int main()
{
  int n,t,i,j=0,ans=0;
  scanf("%d",&n);
  while(n!=0)
  {
      t=n%10;
      i=pow(2,j++);
      ans=ans+t*i;
      n=n/10;
  }
  printf("%d",ans);
}
