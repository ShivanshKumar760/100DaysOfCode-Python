#so for a instance take this code:
x=25
y=50
print("x is :",x)#25
print("y is :",y)#50

#now if have to swap the value of x and y how to do it:
#it can be done in single line with the concept of Assigning Multiple Value to multiple variable:

x,y=y,x
print("after swap")
print("x is :",x)#50
print("y is :",y)#25

#so instead of single line can we write the same line x,y=y,x in two different line like this:

print("Swapping value in diffrent line.")
x=y
y=x
print("x is :",x)
print("y is :",y)
#this code peice wont swap the value cause as we can see firstly we assigned x=y in line 1 what this will do
#is now it will refer to the value of y leaving the value of x and same goes for y:

"""
But what was done in this line of code was different:
x,y=y,x
while assigning the multiple assignments ,remember that python first evaluates the RHS (right hand side )
expression(s) and then assigns them to LHS:

so when we type/write x,y=y,x then python first fetch the value of y and x while reading rhs side and then assign
to LHS.
"""

"""
but if we do want to swap value in different line then we will use the concept of temporary variable

x=25
y=50 
#so before swapping value of x with y we will assign value of x to another variable so that will point to value
#which was given to x and when value of x is swapped we will assign y to temp variable

temp=x
x=y
y=temp
"""
print("Swapping using temp variable")
a=10
b=30
temp=a
a=b
b=temp
print("a is:,",a)
print("b is:,",b)