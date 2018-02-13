import java.util.*;
import java.lang.*;
import java.io.*;
class play80
{
	public static void main (String[] args)
	{
	int a[]=new int[20];
		int n,i,j,min=2000;
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
				if(a[i]-a[j]<min && a[i]-a[j]>0)
				{
					min=a[i]-a[j];
				}
			}
		}
		System.out.println(min);
	}
}
