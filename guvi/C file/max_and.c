#include <stdio.h>
#include<conio.h>
int main()
{
    int a[100],i,j,k,n,max=-1;
    clrscr();
    printf("\nHow many elements???");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("\n%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        for(j=i;j<n;j++)
        {
        k=a[i]&a[j];
        if(k>max)
        {
            max=k;
        }
        }
    }
    printf("\n%d",max);
    getch();
    return 0;
}
