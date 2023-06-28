#! TUPLES
 #! Tuples are unchangable once assigned , ordered , allow duplicate elements 
 #! Tuples are immutable 
 
tuple1 = ("venke",909,True,"guru")
print(tuple1)
print(len(tuple1))    #-----> length of the Tuple declared 
print(type(tuple1))   #classs of the datatype given as tuple 


#tuple constructors are also used to declare tuples

tuple2 = tuple(("venke"))
print("tuple",tuple2)

#! ACCESSING THE TUPLES ls

#! 1. By referring to the Index Number 
#! 2. By Negative Indexing 
#! 3. By Range of Indexes 
#! 4. By checking the condtion using if 

#By refferring the indexnumber 

tuple3 = ("venke",1,2,3,4,"Venkat")
tuplenew= tuple3[5]
print(tuplenew)

#By negavtive Indexing ( Negative indexing which means from the last of the index)
tuplenew = tuple3[-1]
print(tuplenew)

#By range of Indexes

tuplenew = tuple3[1:5:2] #start:end:Step 
print(tuplenew)

#By checking the condition uing if condition 

tuple4 =("venke","GURU","guru","VENKE")
if "venke" or "papa" in tuple4:         
    print("TUPLE4 :",tuple4)
    

#! Python UPDATE TUPLES 

#! Tuples are unchnagalbe and immutable 
#! Immutable - once the values are declared , the object value assingned to it cannot be changed 
#! NOTE : Tuple Datatype are immutable , so they cannot be updated , added , removed once updated
#! Commas are important after a value in tuple orelse it will not be considereed as a tuple 


#Updating the value of the Tuple by converting it to List and then back to tuple 
tuple5 = ("yes","no")
print(tuple5)
list1 = list(tuple5)
list1[1]=["venke"]
tuple5 = tuple(list1)
print(tuple5)

#add Tuple items -- noramally we use insert (), append () to add the value , in tuple convert to list add

tuple6 = ("hi"+"thisis" ,)
print(tuple6)
list2 = list(tuple6)
list2.append("venke")
tuple6 = tuple(list2) 
print(tuple6)

#add tuple to a tuple 

tuple7 = ("hi" , "mynameis")
value1 = ("venke",)
tuple7 += value1
print(tuple7)

#DELETE tuple items and tuple 

# cannot delete tuple as the value once delcared are unchangable - delete by convertingto list 
# REMOVE() keyword is used to dele the value in the lists 
# DEL() Keyword is used to delete the entire tuple

tuple8 = ("venke","guru","VENKAT")
listvalue = list(tuple8)
listvalue.remove("VENKAT")
tuple8 = tuple(listvalue)
print(tuple8)

del tuple8
print(tuple8)

#! UNPACKING A TUPLE 

#create a tuple assing value to it and called packing of tuple 
#we are allowed to unpack the tuple 

fruits = ("apple",1,"orange")   #unpakcing the value assinagned with the other variable 

(push,pull,put) = fruits 
print(push)
print(pull)
print(put)

tuplevalue = (True,False,34,0.19)

(venke,VENKE,guru,GURU) = tuplevalue
print(venke)
print(VENKE)
print(guru)
print(GURU)

#Unpacking the tuple using *ASTERIK 

name = ("venke","guru","sudhakar","venkeguru@gamil",8667498912,"Adharnumber:6801 ")

(firstname,secondname,*mail) = name #----> Variables decarled to unpack
#if the variables less than the values in the tuples *aestrick used to get the values 
print(firstname)
print(secondname)
print(mail)



#! LOOP TUPLES 

#!LOOP thorugh tuples
#!LOOP through indexes 
#! while loop 

tuplename = ("venke1","guru1","hi1") # ------ > looping through the tuples

for name in tuplename:
    print(name)
    print(tuplename)

tuplename1 = ("venke2","guru2","hi2") #looping thorugh Indexes

for name in range(len(tuplename1)):
    print(tuplename1[name])
    
    

#! while Loops 

atuple = ("x","y","z","a","b","c")

value = 1

while (value< len(atuple)):
    print(atuple[value])
    value = value + 1
    
# NOTES: while loop fist gets the inital value to iletrate and then checks the condition and print the value 
# for the next ileration check the value and executes agaian 

#! JOIN THE TUPLES 

#! 1. Join tuples can be done done add operator 
#! 2. Tuples can be muplited into the given time of the values by * operator 

atuple1 = (1,2,3,4,5)         #------> Joining the tuples 
atuple2 = ("x","y","z")
atuple1+atuple2 = tuple3 
print(tuple3)

atuple1 = ("venke","guru")   #-------> Mupltiplying the TUple 
tuple3 = atuple1 *2 
print(tuple3)


#! Tuple methods 

#Tuple datatype have two built in methods and they are
#1. COUNT()
#2. INDEX()




