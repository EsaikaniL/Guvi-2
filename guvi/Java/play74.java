import java.util.*;
import java.lang.*;
import java.io.*;
class play74
{
	public static void main (String[] args)
	{
		String pk;
		System.out.println("Enter Your String...");
		Scanner in=new Scanner(System.in);
		pk=in.nextLine();
		int i,j,c=0;
		int n;
		char [] st=pk.toCharArray();
		n=pk.length();
		for(i=0;i<n-1;i++)
		{
			for(j=i+1;j<n;j++)
			{
				if(st[i]==st[j])
				{
					c=1;
					break;
				}
			}
		}
		if(c==1)
		{
			System.out.println("Yes");
		}
		else
		{
			System.out.println("No");
		}
	}
}
