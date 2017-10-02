str=raw_input('Enter the string:\n')
enc=''
dec=''
choice=int(input('Enter ur option:\n1.Encription \n 2.Decrption \n' ))
if choice==1:
	for x in range(0,len(str)):
		enc=enc+chr(ord(str[x])-3)
	print enc
else:
	for x in range(0,len(str)):
		dec=dec+chr(ord(str[x])+3)
	print dec
