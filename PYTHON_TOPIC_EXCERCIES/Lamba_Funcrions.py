#LAmba Functions are small anomymns functions 
#! They are funtions that take any number of Arguments but one only expression 

# SYNTAX : lamba arguments : expression 

# 1. arguments are the input paramter for the function 
# 2. Expression is the condition to be executed with the inputs 


# Lambda can take any number of Arguments 

x = lambda a : a + 10  
print(x(5))

x1 = lambda a,b,c : a+b+c
print(x1(3,4,5))


# Program to calculate Lambda using a Function and Lambda 
# FUCNTION 

def square_number(n):
    
    return n*n

square_number(5)

# using LAMBDA 

square = lambda x : x **2 
print(x(2))



