
#! WHile Loops are the loops that will be executed untill the  condtion is False

#Synatax :

#while condition :


# Print i as long as i is less than  6

i = 1 
while(i < 6):
    print(i)
    if (i==6):
        print("done")
    i+=1
    
#! BREAK Statement which can stop the loop even the condition i true 

i = 1
while i<6:
    print(i)
    if i == 4:
        break 
    i+=1
    
#! Continue statement can stop the current iletarion and  ontinue with the next 

i = 0

while i < 6:
    i=+1
    if i ==3:
       continue
    print(i)
    
#! The else statement in the while loop 

i = 1 
while 1 <6 :
    print (i)
    i+=1
else :
    print("is longer less than 6 ")   
    


    
