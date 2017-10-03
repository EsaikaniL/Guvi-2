str1=raw_input('Enter any string(Must contain numbers)')
str=list(str1)
s1=[]
mul=0
sum1=0
sum2=0
ad=1
for x in str:
	if x.isdigit():
		s1.append(int(x))
a=max(s1)
for x in s1:
	mul=mul+(x*a)
while (mul!=0):
	t=mul%10
	sum1=sum1+t
	mul=mul/10
if (sum1>9):
	sum3=0
	while (sum1!=0):
		t=sum1%10
		sum3=sum3+t
		sum1=sum1/10
	sum1=sum3
b=min(s1)
for x in s1:
	ad=ad*(x+b)
while (ad!=0):
	te=ad%10
	sum2=sum2+te
	ad=ad/10
if (sum2>9):
	sum4=0
	while (sum1!=0):
		t=sum2%10
		sum4=sum4+t
		sum2=sum2/10
	sum2=sum4
k=min(sum1,sum2)
print k*k
