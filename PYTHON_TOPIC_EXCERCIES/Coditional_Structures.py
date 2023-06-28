
#! If condition used 

x,y = 100,100
if x>y:
        result = "the given numbers are equal"
        print(result)
else:
        result="the given numbers are not equal"
        print(result)
        
if __name__ == "__main__": 
   main()  

#! 2 #Elif condtion used         
x,y = 100,100

if x>y:
   result = "x is greater than y"
elif x==y:
   result="x is equal to y"
elif x + y :
   result ="x is additon of y"
else:
   result ="y is greater than y "
print(result)

#!3. condition used in simple line 

x = 65.8
y = 65.9

result = "x is the smallest " if x ==y else " Y is the biggest"
print(result)


#! 4match case which is used to compare multiple values

value = 89
match value:
     case "one":
        result = 1
     case "two":
        result = 2
     case "three":
        result = 3
     case "four "|"five":
        result = (4,5)
     case _:
        result="default"
    
print(result)


value = (20)
match value:
   case 10:
       output="10"
   case 20: 
       output ="venke"
   case _:
       output ="default"
print("output")
   
