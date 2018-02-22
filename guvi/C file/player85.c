#include <stdio.h>
#include<conio.h>
int main()
{
    int a;
    clrscr();
    printf("Enter the number:");
    scanf("%d",&a);
    printf("The bitwise not of a number is:%d",~a);
    getch();
    return 0;
}
