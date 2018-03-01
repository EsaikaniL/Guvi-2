#include <stdio.h>

int main()
{
  int n,t,ans=0;
  scanf("%d",&n);
  while(n!=0)
  {
      t=n%2;
      ans=ans*10+t;
      n=n/2;
  }
  printf("%d",ans);
}
