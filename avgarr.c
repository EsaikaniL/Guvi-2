#include <stdio.h>
 
int main(void) {
	int a[10],sum=0,i,n;
	float avg;
	printf("How many elements...");
	scanf("%d",&n);
	printf("Enter the array:\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
    for(i=0;i<n;i++)
    {
    	sum=sum+a[i];
    }
    avg=sum/n;
    printf("sum of array is:%f",avg);
	return 0;
}
