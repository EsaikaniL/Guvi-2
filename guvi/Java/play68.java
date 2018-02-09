import java.util.*;
import java.lang.*;
import java.io.*;
class play68
{
	public static void main (String[] args) throws java.lang.Exception
	{
	
		int a[]=new int[20];
		int b[]=new int[20];
		int n,i,j,f;
		Scanner in=new Scanner(System.in);
		System.out.println("How many elements??");
		n=in.nextInt();
			System.out.println("\nEnter the elements..");
		for(i=0;i<n;i++)
		{
				a[i]=in.nextInt();
		}
	for(i=0;i<n-1;i++)
	{
		f=0;
		for(j=i;j<n;j++)
		{
		if(a[j]==a[i])
		{
			f=f+1;
		}
		else if(a[j]!=a[i])
		{
		break;
		}
		}
	b[i]=f;
	}
	int max=-1;
		for(i=0;i<n-1;i++)
	{
		if(b[i]>max)
		{
			max=b[i];
		}
	}
	System.out.println(max);
	}
}
