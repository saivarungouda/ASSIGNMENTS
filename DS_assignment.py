#string data structures

str="alladi cloud training"
#W.P.P. to find len() of the string
print("length of the string is:",len(str))
#W.P.P to find index() of the "cloud"
print("string indexing :",str.index("cloud"))
#W.P.P to apply find() function to locate "training"
print("finding a element in a string:",str.find("training"))
#W.P.P to demonstrate lstrip() and rstrip() and strip() methods to remove extra spaces from the input string given at runtime?
str1=input("enter a string to perfom strip operation:")
print(str1.strip())

str2=input("enter a string to perfom right strip operation:")
print(str2.rstrip())

str3=input("enter a string to perfom left strip operation:")
print(str3.lstrip())

#W.P.P. to covert given string into upper(0, lower(), capatalize(), title(),swapcase()
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.swapcase())
#W.P.P. to check given character type such as isdigit() or space() or isalpha() isalnum() or islower() or isupper()
print(str1.isdigit())
print(str.isspace())
print(str.isalpha())
print(str.isalnum())
print(str.islower())
print(str.isupper())