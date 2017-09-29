#include <stdio.h>
 
int main(void) {
	int n1,n2,*n3,*n4,sum;
	printf("Enter the number:\n");
	scanf("%d%d",&n1,n2);
	n3=&n1;
	n4=&n2;
	sum=*n3+*n4;
	printf("Addition is:%d",sum);
	return 0;
}
