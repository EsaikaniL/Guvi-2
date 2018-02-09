import java.util.*;
import java.lang.*;
import java.io.*;
class play71
{
	public static void main (String[] args) throws java.lang.Exception
	{
		
		int a[]=new int[20];
		int i,n;
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
		if(a[i]<a[i+1])	
		{
			System.out.println(a[i+1]);
		}
		else
		{
				System.out.println(a[i]);
		}
		}
	}
}
