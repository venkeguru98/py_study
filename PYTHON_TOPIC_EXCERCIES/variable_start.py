#DATA TYPES AND VARIABLES 

myint = 10 
myfloat = 3.14 
str1 ="venke"
mylist =[ 10,"venke",20,3.00]

mytuple=(0,1,"venke")

mydict1= { "NAME": "venkat" , "GENDER" : "MALE" , "AGE" : 25 }
mydict2= { "NAME" : "YYY" ,"GENDER" : "FEMALE" , "AGE" : 26}

print("DICITIONARY")
print(mydict1)
print(mydict1["NAME"],mydict1["GENDER"])
print("LIST")
print(mylist)
print("TUPLE")
print(mytuple)
print("INDEXING")
print(mylist[0])
print(mytuple[-3]) #Negative Indexing 
print("SLICING")
string1 = "helloworld"
print(string1[0:2])
print(string1[:-1:2]) # - end Takes the end value from the last 
print(string1[::-1])#Reverses the given String 
print(string1[::1])# --- Returns the same string 

#----------------#FUNCTION--------------------------#
#Local Variable decalred in the function takes the varaible 
#which is declared insdie the function

#if the Variable needed to global , is should be called or sepcifed to access 
#or look for the Global variable 
 
print("FUNCTION")
def somefunction():
    global str1
    str1 = "Hello world"
    print("Function Working",str1)
somefunction()
print(str1)

def samplefunction():
    
    mylist=[5,10,15]
    print(mylist)

samplefunction()
print(mylist)    

  





