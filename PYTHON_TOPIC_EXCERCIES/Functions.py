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



    
    
    