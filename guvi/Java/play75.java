import java.util.*;
import java.lang.*;
import java.io.*;
class play75
{
	public static void main (String[] args)
	{
		int a[]=new int[20];
		int n,i,j,ct=0;
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
			for(j=i+1;j<n;j++)
			{
				if(a[i]<a[j])
				{
					ct++;
				}
			}
		}
		System.out.println(ct);
	}
}
