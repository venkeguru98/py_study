#1.Define a Basic Function 

def simplefunction():
    print("Function block executed")
    return 0
    
simplefunction()
print(simplefunction)
print(simplefunction())

#2.function that takes arguments 

def function2(arg1,arg2):
   
    print(arg1, " "  ,arg2)
    
function2(10,30.03)

#3. Functions that Returns a value in the end 

def cubesquare (x):
    return x*x*x


print(cubesquare(4))  

#4.function with default value for the Argument 

def function3(val1,val2=0):
    result =1 
    for i in range (val2):
        print(i)
        result = result * val1
    return result

print(function3(2))

#5.function with variable number of arguments (ie : more number of arguments )
def function_multi_ADD(*value):
    result =0 
    for i in value :
       result = result + i 
    return result

print(function_multi_ADD(2))

#6.Write a function named "calculate_average" that takes a list of numbers as an argument 
#and returns the average of those numbers


def calculate_average(given_numbers):
    total = 0
    for number in given_numbers:
        total += number
    return total / len(given_numbers)

given_numbers=(20,20,20,20,20)
print(calculate_average(given_numbers))       

print("enter the number")


#! Functions can be made in arguments 

#Arguments are information passed in the functions 

def afunction(name):
    print("the name of the given " + " " ,name)

afunction ("venke")
afunction ("VENKAT")


#! ir the number of args are undefined *args are used to access the function and when 
# *args are used they act as tuple and accessed by the tuuple indexes 



def argfunction (*names):
    print("the Name to be displayed is ",names[0])
    
argfunction("venke","venkat","guru")


#2 

def alistfunction (*numbers):
    for number in numbers:
        print(number)
    

alist = [1,2,3,4,5]
alistfunction(*alist)


#KEYWORD ARGUMENT = ** double astreisk used in keyarguments 
#synatax key = value 

#1
def keywordargument (value2,value1,value3):
    print("The name of the student 2 is",value2)
    
    
keywordargument(name="venke",name2="guru",name3 ="venkat")

#2 - CALCULATE THE TOTAL COST OF ITEM with any discounr and taxes



def calulate_the_total_cost (itemprice,qunatity,totalpercent=0,totaltax=0):
    total_cost = itemprice * qunatity
    total_cost -= total_cost * totalpercent/100
    #total_cost = totalcost+totalpercent/100
    total_cost += total_cost * totaltax /100
    
    return total_cost


total = calulate_the_total_cost(100,5)
print(total)

#2 CALCULATE_AVERAGE

def calculate_average (listvalues):
    
    sum =0
    count =0 
    for value in listvalues:
        sum = sum + value 
        count = count + 1
        
    average = sum /count 
    return average    

listvalues = [1,2,3,4,5]
result = calculate_average(listvalues)
print(result)


#3 - arbitary keyword arguments 

#if the number of keys words are unknown ** are used 

def argkeyword_function (**value):
    print("the middle name is dispalyed as",value["middlename"])
    
argkeyword_function(firstname ="venkat",lastname = "sudhakar",middlename ="guru")

#4 

def print_the_value (**values):
    for key,value in values:
        value_to_print =print(f"{key} :{values}")
        return value_to_print
        
    
    result = print_the_value(name="venke",age = 32,class_std ="fifth")



#DEFAULT PARAMTER VALUE 

# if you call the function without any arguments it will take the assinged argument 


def defparameter ( name = "venke"):
    
    print(name)

defparameter("venkat")
defparameter("venkee")
defparameter("venke") 


#2 - if the paramter is not passed 

def aname(name,message ="hi"):
    print(f"{name},{message}")
    
aname("venkat")
aname("venke","hi1")s


#Return value ---> to return a vlue in a function use RETURN STATEMENT 

def calculatesqaure (x):
    return x*x

calculatesqaure(5)


#THEPASS Statekment the Funcrion block cannot be empy and so 
#Pass statemnent is ued and it do not through any error 
# A FUNCTION CALLING ITSELF IS KNOW AS RECURSVE FUNCION 

# TYPES - BASE CASE amd RECURSIVE BASE 

#base case---> Terminating from  recursive
#recursive case --->calling itself in the function  


#example Factorial of a number 

def factorail(n):
    if n ==0 or n ==1:
        return 1 
    else:
        return n * factorail(n-1)
    
num = 5 
result = factorail(num)
print(f"The factorail of {num} is {result}")
        

















    
    
    