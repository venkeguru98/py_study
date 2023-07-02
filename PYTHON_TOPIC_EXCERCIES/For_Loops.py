#! For Loops are used to Iletrare 


names = ["venke","venkat","guru"]

for i in names : 
    print (i)


#The Break Statemnet in the loop , WHich break the iletraion in the condition if TRUE 

name = ["venke","VENKAT","Guru"]

for names in name :
    print (names)

    if names == "VENKAT" :
        break 

# THe BREAK STATEMENTS STOPS THE LITERATION 

# CASE 2 : Break statement stops the ilteario and then Prints the value 

name = ["venke","VENKAT ","Guru"]

for names in name :
    if names == "Guru":
        break 
    print(names)

#OUTPUT : venke , VENKAT 

#THE CONTINUE STATEMENT which check for the condition and if True skips the Iletairation and continues

name = [ "venkat","venke","guru"]

for names in name :
    print( names)

    if names == "venke":
        continue 

#CASE 2 : 

name = [ "venkat","venke","guru"]

for names in name :
    

    if names == "venke":
        continue 
    print( names)


#THe RANge FUnction which gives the iltearion from 0 to the given valuye 

for i in range (1,6):
    print(i)


# NESTED FOR LOOP 

#NESTED FOR LOOP in which for loop within a loop and for very iletration the other loop executes 

for i in range (1,5):
    for j in range ((1,5)):
        print (i,j)
