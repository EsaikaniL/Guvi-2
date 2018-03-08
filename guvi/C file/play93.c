#include <stdio.h>

int main()
{
    int n,a[20],t,temp,i;
  scanf("%d",&n);
  for(i=0;i<n;i++)
  {
      scanf("%d",&a[i]);
  }
  t=a[0];
  for(i=0;i<n-2;i++)
  {
     temp=a[i];
     a[i]=a[i+1];
  }
  a[n-2]=t;
  for(i=0;i<n;i++)
  {
      printf("\n%d",a[i]);
  }

    return 0;
}
