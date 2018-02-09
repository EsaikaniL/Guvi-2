import java.util.*;
import java.lang.*;
import java.io.*;
class play72
{
	public static void main (String[] args) throws java.lang.Exception
	{
	ArrayList a=new ArrayList();
	int i,n,k,p;
	Scanner in=new Scanner(System.in);
	n=in.nextInt();
	for(i=0;i<n;i++)
	{
		k=in.nextInt();
		a.add(k);
	}
	Collections.sort(a);
	
	System.out.println(a.get(n/2));
	}
}
