"""
there are total two way to do this 
1)use of operator 
	num=39
	rem1=num%10#9
	num=num//10#3
	print(rem1+num)

	this will give the correct output but the problem is 
	we have not studied about operator till now so we will
	use 2nd Method.

2)convert int to string and use index to access individual
element
	num=39
	num=str(num)
	print(int(num[0])+int(num[1])
	"""

num=29
num=str(num)
print(int(num[0])+int(num[1]))
