# Python Conditions and IF statements 

#Equal a ==b
#Not Equal a !=b
#less than a<b
#greater Than a>b
# Greater than equal to a>=b
# less than equal to a<=b

#! NOTE : INDENTATION to define the scopoe in the code 

#! IF ELSE STATEMENTS 

a = 30
b = 20 

if a >b :
    print(" a is greater")


#! Elif condtiton is used when the previous condition were not true , saying to try this conditon

a = 33
b = 20

if a < b:
    print("a is lesser than b")
elif a >b :
    print ("a is greter than b ")
    
#! Else is which the block is exected if any og the given condititon are True 

a = 20 
b = 10 

if a == b :
    print("a is equal to b ")
    
if a * b == 20 :
    print ("a is multiple of b and prod is 200")
    
else :
    print ( " all conditions are false ")
    
#! Short hand if and if else 

if a > b : print("a is greater ")

a = 20 
b = 20 

print("a") if a >b else print ("b")

#! CONDTITIONAL STATEMENTS 

# This is also called ternary operator or condirional statement 

# AND # OR # NOT are some of the condititonal statement 

a = 40
b = 30

print( "A is Greatear") if a > b else print (" B is Greatest ") 

#! NESTED IF  

# Having if statement inside the if statement , this is called nested if 

a = 30 


if ( a > 10): 
    print( " a is Greater ")
    if (a > 30) : 
        print("a is greater than 30") 
    else :
        print("all condition are False")
        
#! PASS STATEMENT 

# if statements cannot be empty , but if you fr some reason have an if statement with no content
# put in the pass statement to avoid error






