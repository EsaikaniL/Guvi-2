#include <stdio.h>
#include,conio.h>
int main()
{
    int a[100],n,i,ans;
    clrscr();
    printf("How many elements???");
    scanf("\t%d",&n);
    printf("\nEnter the elements\n");
    for(i=0;i<n;i++)
    {
       scanf("%d",&a[i]); 
    }
    ans=a[0];
    for(i=1;i<n;i++)
    {
        ans=ans|a[i];
    }
    printf("\nAns:%d",ans);
    getch();
    return 0;
}
