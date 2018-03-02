#include <stdio.h>

int main()
{
  int n,t,i,a[255],k=0;
  scanf("%d",&n);
  while(n!=0)
  {
      t=n%2;
      a[k++]=t;
      n=n/2;
  }
  for(i=k-1;i>=0;i--)
  {
      printf("%d",a[i]);
  }
}
