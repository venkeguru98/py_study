#Membership Operators
#in and not in are the membership operators;
# used to test whether a value or variable is in a sequence.

x = 10
y = 30
list = [ 10,30,40,50]
if x in list:
   print("The value of x is in sequence")
else:
   print("The value of x is not in seqeunce")
   
if y in list:
   print("The value of %d is in sequence" %(y))
else:
   print("The value of %d is not in sequence", (y))

#----------------------------------------------------------#

#identity Operator

#is and is not are the identity operators both are used 
#to check if two values are located on the same part of the memory

a = 10
b = 20
c = a
print(c is a )
print(c is not a)
print(a is not b)

a = "venkat"
b = " YYY"
c = " YYY" #identity operator looks for the same memory location is used 
print(a is not b )
print(b is c )

#-------------------------------------------------------------
#Operator PRESCEDENCE 

exp1 = (10+20*30/28*5)
print(exp1)

str1 = "venke"
val1 = 20 

if str1 =="venke" and str1 =="YYY" and val1>=30 :
   print("entry")
else:
   print("exit")  


