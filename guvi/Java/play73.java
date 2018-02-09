import java.util.*;
import java.lang.*;
import java.io.*;
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		int a[]=new int[30];
		int n,i,k;
		System.out.println("How many elements???");
		Scanner in=new Scanner(System.in);
		n=in.nextInt();
		for(i=0;i<n;i++)
		{
		a[i]=in.nextInt();	
		}
		System.out.println("\nEnter K value...");
		k=in.nextInt();
		for(i=0;i<n;i++)
		{
		if(a[i]==k)
		{
			break;
		}
		}
		System.out.println("\n"+(i+1));
}
}
