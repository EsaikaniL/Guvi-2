import java.util.*;
import java.lang.*;
import java.io.*;
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
	
		int a[]=new int[20];
		int n1,n2,i,j,tp;
		Scanner in=new Scanner(System.in);
		System.out.println("How many elements in Array1??");
		n1=in.nextInt();
			System.out.println("\nEnter the elements..");
		for(i=0;i<n1;i++)
		{
				a[i]=in.nextInt();
		}
			System.out.println("How many elements in Array2??");
			n2=in.nextInt();
			System.out.println("\nEnter the elements..");
		for(i=n1;i<n1+n2;i++)
		{
				a[i]=in.nextInt();
				
		}
		for(i=0;i<(n1+n2)-1;i++)
		{
			for(j=i+1;j<n1+n2;j++)
			{
				if(a[i]>a[j])
				{
					tp=a[i];
					a[i]=a[j];
					a[j]=tp;
				}
			}
			
		}
			for(i=0;i<n2+n1;i++)
		{
				System.out.print(a[i]+" ");
				
		}
		
		
	}
}
