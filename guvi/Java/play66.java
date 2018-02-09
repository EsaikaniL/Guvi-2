import java.util.*;
import java.lang.*;
import java.io.*;
class play66
{
	public static void main (String[] args) throws java.lang.Exception
	{
		int a[]=new int[20];
		int n,i,k,j,f;
		Scanner in=new Scanner(System.in);
		System.out.println("How many elements??");
		n=in.nextInt();
			System.out.println("\nEnter the elements..");
		for(i=0;i<n;i++)
		{
				a[i]=in.nextInt();
		}
		System.out.println("\nEnter the K value...");
		k=in.nextInt();
	for(i=0;i<n;i++)
	{
		f=0;
		for(j=i;j<n;j++)
		{
		if(a[i]==a[j])
		{
			f=f+1;
		}
		}
		if(f==k)
		{
			System.out.println("\n"+a[i]);
		}
	}
	}
}
