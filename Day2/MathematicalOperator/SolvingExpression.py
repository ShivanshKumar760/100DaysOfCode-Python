Expression1=3*3+3/3-3
"""
in this multiplication and division have same 
precedence and addition and subtraction have same 
precedence so the operator at left most will be operated 
irst which is * then division and then +

9+3/3-3
9+1-3
10-3

"""
print(Expression1)

Expression2=3*(3+3)/3-3


"""
and now if we use paranthesis like 

exp=3*(3+3)/3-3 in this case first the bracket 
part will be solved first

3*(6)/3-3 Now Multiplication 
18/3-3 division
6-3
3
"""
print(Expression2)