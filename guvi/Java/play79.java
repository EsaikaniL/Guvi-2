import java.util.*;
import java.lang.*;
import java.io.*;
class play79
{
	public static void main (String[] args) throws java.lang.Exception
	{
	int a[]=new int[20];
		int n,i,j,max=-1;
		Scanner in=new Scanner(System.in);
		System.out.println("How many elements??");
		n=in.nextInt();
			System.out.println("\nEnter the elements..");
		for(i=0;i<n;i++)
		{
				a[i]=in.nextInt();
		}
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{
				if(a[i]-a[j]>max)
				{
					max=a[i]-a[j];
				}
			}
		}
		System.out.println(max);
	}
}
