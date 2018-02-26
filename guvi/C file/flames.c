#include<stdio.h>
#include<string.h>
void main()
{
	char a[200],b[200],f[10]="flames",f1[10];
	int l1,l2,l3,l4,i,t1,j,k,p,m,q,flag=0,n;
	printf("Enter your name:");
	gets(a);
	printf("\nEnter your partner name:");
    gets(b);
    l1=strlen(a);
    l2=strlen(b);
	for(i=0;i<l1;i++)
	{
		for(j=0;j<l2;j++)
		{
			if(a[i]==b[j])
			{
				a[i]='*';
				b[j]='*';
				break;
			}
		}
	}
	for(i=0;i<l1;i++)
	{
		if(a[i]!='*')
		{
			p++;
		}
	}
	for(i=0;i<l2;i++)
	{
		if(b[i]!='*')
		{
			q++;
		}
	}
	if(p+q==0)
	{
		printf("\nYou entered same name!!!!");
	}
	else if(p+q==1)
	{
		printf("\nYou are sister or brother!!!!");
	}
	else
	{
	for(k=0;k<5;k++)
	{
		i=0;
		t1=0;
		n=1;
		if(flag==1)
		{
		l3=strlen(f);
		for(m=0;m<l3;m++)
		{
			f[m]='\0';
		}
		l4=strlen(f1);
		for(m=0;m<l4;m++)
		{
			f[m]=f1[m];
		}
		for(m=0;m<l4;m++)
		{
			f1[m]='\0';
		}	
		}
		l3=strlen(f);
		while(n<=p+q)
		{
		flag=1;
		if(i==l3-1)
		{
			i=0;
			}	
		else{
			i++;
		}
		n++;
		if(n==p+q)
		{
			for(m=i+1;m<l3;m++)
			{
			f1[t1++]=f[m];	
			}
			for(m=0;m<i;m++)
			{
			f1[t1++]=f[m];	
			}
		}
		}
	}
	if(f1[0]=='f')
	{
		printf("\nYou are friends!!!!");
	}
	else if(f1[0]=='l')
	{
		printf("\nYou are Lovers!!!!");
	}
	else if(f1[0]=='a')
	{
		printf("\nYou have affection!!!!");
	}
	else if(f1[0]=='m')
	{
		printf("\nYou will marry!!!!");
	}
	else if(f1[0]=='e')
	{
		printf("\nYou are Enemies!!!!");
	}
	else if(f1[0]=='s')
	{
		printf("\nYou are sister!!!!");
	}

}
}
