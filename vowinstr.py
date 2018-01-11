st=input("Enter any String:")
vow=['a','e','i','o','u','A','E','I','O','U']
flag=0
for x in st:
	if x in vow:
		flag=1
if(flag==1):
	print("Vowel is present")
else:
	print("Vowel is not presented")
