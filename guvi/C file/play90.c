#include <stdio.h>

int main()
{
  int n,i,k,k1=1,k2=1,k3=1;
  float ans;
  printf("Enter");
  scanf("%d%d",&n,&k);
  for(i=1;i<(n+1);i++)
  {
    k1=k1*i;  
  }
  for(i=1;i<(n+1)-k;i++)
  {
    k2=k2*i;  
  }
  for(i=1;i<(k+1);i++)
  {
      k3=k3*i;
  }
  ans=k1/(k2*k3);
  printf("\n%.2f",ans);
    return 0;
}
