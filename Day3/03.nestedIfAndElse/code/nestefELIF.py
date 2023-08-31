age = int(input("Enter the age :"))
height=int(input("Enter the height :"))
if(height>=120):
	print("Allowed to ride the coster")
	if(age < 12):
		print("pay 5 rs")
	elif(age<=18):
		print("pay 20 rs")
	else:
		print("pay 50 rs")
else:
	print("Not allowed")