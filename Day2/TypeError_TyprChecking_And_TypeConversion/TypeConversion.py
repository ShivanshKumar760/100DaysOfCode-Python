num=123
print("num is:",type(num))
Convert_num_to_str=str(num)
print("num is :",type(num))
n1=1
print("value of n1 is :",n1)
print("n1 is :",type(n1))
n1_to_bool=bool(n1)
print("value of n1 is :",n1_to_bool)
print("n1 is :",type(n1_to_bool))
stringValue="30"#in python if we try to convert a string with
#alphabet into integer it will give error saying

"""
ile "/Users/mac/Desktop/Python/100DaysOfPython/Day2/TypeError_TyprChecking_And_TypeConversion/TypeConversion.py", line 12, in <module>
    String_to_int=int(stringValue)
ValueError: invalid literal for int() with base 10: 'a'


thats because we cannot convert alphabet into int value un
-like other programming language where when we do this we 
get ascci value in python for that we have special inbuilt
function ord()

"""
String_to_int=int(stringValue)
print("String Value in int is:",String_to_int)
print("String Value is :",type(String_to_int))