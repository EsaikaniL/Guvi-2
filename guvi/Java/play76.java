import java.util.*;
import java.lang.*;
import java.io.*;
class play76
{
	public static void main (String[] args)
	{
	int a[]=new int[20];
	int b[]=new int[20];
	int c[]=new int[20];
		int n,i,j,ct1=0,ct2=0;
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
			if(a[i]%2==0)
			{
				b[ct1]=a[i];
				ct1++;
				
			}
			else
			{
				c[ct2]=a[i];
				ct2++;
			}
		}
		if(ct1<ct2)
		{
			System.out.println(b[0]);
		}
		else
		{
			System.out.println(c[0]);
		}
	}
}
