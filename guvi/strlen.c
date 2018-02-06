#include <stdio.h>

int main(void) {
	char var[20];
	int i;
	printf("Enter the string \n");
	scanf("%s",&var);
	for(i=0;var[i]!='\0';i++);
	printf("%d",i);
	return 0;
}
