print("Welcome to the tip calculator!")

bill=float(input("What was the total bill? $"))

tip=int(input("How much tip would you like to give? 10, 12, or 15? "))

number_to_split=int(input("How many people to split the bill?"))

"""
suppose we want to give a tip of
12 percent ie 12/100=0.12

and then we need to multiply 0.12 to 150 cause we need togive 12 percent of 150 

150*0.12=18.0
now tip is added into total
150+18.0=168.0


or what we can do here is:
150 +(150*0.12) if we take 150 as common

150(1+0.12)--150*1.12

"""
tip_as_percentage=tip/100
total_bill=bill*(1+tip_as_percentage)

bill_per_person=total_bill/number_to_split

final_amount=round(bill_per_person,2)

print(f"Each person should pay {final_amount}")
