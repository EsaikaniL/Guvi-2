#include <stdio.h>
#include<conio.h>
int main()
{
    int a[100],i,n,ans;
    clrscr();
    printf("\nHow many elements???");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("\n%d",&a[i]);
    }
    ans=a[0];
    for(i=1;i<n;i++)
    {
        ans=ans&a[i];
    }
    printf("\n%d",ans);
    getch();
    return 0;
}
