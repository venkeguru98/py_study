#1.-------------------@VARIABLE NAMES@----------------------------------------------------------#
myName="john" #CAMEL CASE ( which execept first starts with capital letter)
MyName="john" #Pascal Case(Each letter starts with caps)
my_name="john" #Snake case (separted with underscore)
print(myName,MyName,my_name)

#2. ----------Convert one data type to another data type  --------------------------------------#

x = 10
y = 2.0
a = float(x)
b = str("y")
print(a,b)
print(type(a),type(b))


#3.-------@STRING SLICING - cetain value of indexes can be returned with the start and end index ---#

a = "venkat"
print(a[1:5],a[2:4])  #........ Output - enka nk 

b = "gurunathan"  
print(b[-4:-1])       #.......... > Negative slicing takes form the end
                                     
c = "gurunathan"
print(c[-5:-2])

#4 ---------------------@Modify and Format Strings-------------------------------------------------#
   
   #write a progam to convert small letter to upper case , Upper case to lower case 
   
a = "venkaTesh"

print(a.upper(),a.lower())

   #Write a program to concentate two strings
a = "venkatesa"
b ="Gurunathan"
print(a+" "+b)

#reverse a string 

