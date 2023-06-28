#list datatype are ordered,Changabele and Allow Duplicates 

#!1 Python Lists 

list0 = [ "venke",5, "venke"]                  # Lists 
print(list0)

list1 = ["venke",5, "venke"]                   #----------> Length of the List 
listnew= len(list1)
print(listnew)

list2 = ["venke",5, "venke"]                   #------> Type of the List 
listtype = type(list2)
print(listtype)

namelist = list(("name","venkat","school"))    #----> CONSTRUCOTR (())
print(namelist)


#! Accessing the List Items 


mylist = ["venkat","guru","venke"]              #accessing by values 
print(mylist[1],mylist[0])

mylist1 =["venke","guru","guru" ]              #--------> Indexing access
newmylist1=mylist1[::-1]
print(newmylist1)

mylist2 = ["venke","guru","guru"]
if ("xxx") in mylist2:
    print("yes present")
else:
    print("not present in llist ")
    
elif:
    print(mylist2)
    
    
#! Chnage liat Items 

mylist3 = ["venke","guru","venkat"]
mylist3[1:3] = [ "XXX","YYY"]
print(mylist3)

mylist4 = ["venke","guru","venkat","venkat"]  #if the given slicing is less or more than that of the declared variable the remaing vakue will be also returned 
mylist4[1:3] =["VENKAT","VENKAT"]   # change the Second and Third word using the given list name
print(mylist4)


mylist5 = ["venke","guru","XXX"] # insert key words just inserts a new list name wihout Replacing 
mylist5.insert(0,"ZZZ")  #Insert only accepts two arguments 
print(mylist5)

mylist6 = ["venke","guru","venkat"]  # inserting the two value only index slicing methods can be used 
mylist6[0:0] = ["XXX","YYY"]
print(mylist6)

#! ADDING THE LISTS 
#! append() 
#! extend()
#! Insert()

mylist7 = [10,20,30]
mylist8 = [10,20,30]

myresultlist =[]
for i in range (len(mylist7)):
    myresultlist.append(mylist7[i]+mylist8[i]) #append which is used to add at the end of the list 
print(myresultlist)


mylist9 = ["venke","guru","venke"]
mylist9.insert(3,"guru") #----> insert which isused to insert the list in the index value given in arument 
print(mylist9)

mylist10=["venke",1,2]
mylist10.extend(("guru1","guru2")) #extend is used to add other list with the cuurent list 
print(mylist10)

mylist11=[3,4,5]
mylist10.extend(mylist11)
print(mylist10)

mylist26 = ["venke","guru","VENKAT","GURU"]

mynewlist=[]
for i in mylist26:
    if "v" in i :
        mynewlist.append(i)
        print(mynewlist)
        
        
 #! (extend) method which can be used iterable objects ( sets,tuple,dictinoary) 
 
 #! DELETING THE LISTS 
 #! remove() - removes the specified item 
 #! pop() - removes the speocifef index , if not mentioned the index removes the last item
 #! del() - delets the sperfieed index or not speicided delets the entire list 
 #! clear() - keywords empties the content but the table stay 
 
 
mylist12 = ["venke","guru","venkat"]  
mylist12.pop(2)   #----> Specified index value is given to remove the value in the list 
print(mylist12) 

mylist13= ["venke","guru","venkat"]   
mylist13.remove("venkat") #-----> Remove with the specified value in the list 
print(mylist13)


mylist14=["venke","guru","venkat"]
del mylist14[0]    #----> Remove the values of the list by sepcified index 
print(mylist14)

mylist15=["venke","guru","venkat"]
del mylist15
#print(mylist15)  #--------> delets the whole list 

mylist16=["venke","guru","venkat"]
mylist16.clear()  #----------> Removes the contents but the list remains 
print(mylist16)


#! LOOPS in LISTS 



mylist17 = ["venke","guru","venkat"]  
for x in mylist17:  # ----> Loop used to print each value in order 
    print(x,mylist17)
    
mylist18 = [1,2,3,4,5,6,7,8,9,10]
for num in range (len(mylist18)):   #in this example it ileratrates in the range 0 to 9 with the value in the list 
    print(mylist18[num])
    
mylist20 = [ 100, 200, 300]
for y in range (len(mylist20)):# ilerates the value in loop and prints the value of ileration from 0 to 2
    print(y)   
    
    
mylist19=[80,100,20,10,50]
for i in range(len(mylist19)):# in the range from 0 to 4 , prints the value i the list 
    print(mylist19[i])
    
#! WHILE LOOPS USING LISTS


# SYNTAX OF WHILE LISTS

#while (Condition) = True ----> Block executes 
#Do_someting()

# While loop runs untill the condition gets false which the initate value vs the condition  
mylist21= [10,20,30]
value  = 0
while value in range(0,3):
    print(mylist21[value])
    value=value+1 
    
mylist22 = ["venke","guru","VENKAT","GURU","venke","guru"]

i = 0
while i < (len(mylist22)):
    print(mylist22[i])
    i =i+2
    

#! LIST COMPREHESNION 


# new_list = [expression for item in iterable if condition]
# In this expression:

# expression is the value or operation to apply to each item in the iterable (e.g. item*2)
# item is a variable that represents each item in the iterable
# iterable is the original collection of values (e.g. a list, tuple, or string)
# condition is an optional filter that specifies which items should be included in the new 

#! SYNTAX : list = [expression_for item_in iterable if condition]
#! EXPRESSION - Current item in the iletration and the final outome 
#!The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:


mylist23 = [10,20,30,40,50,60,70]
[print(mylist23[i]) for i in range(1,5)] #----> print the values in loop 

mylist24 = [1,2,3,4,5,6]
Reverse_order = [mylist24[i] for i in range(len(mylist24)-1,-1,-1)]

print(Reverse_order)    # Reversing the list using list comphresion 
print(mylist24)


mylist25 = [1,2,3,4,5,6,7,8,9,10]   #to print the newlist with values divible by 2 and mutiple with 2
newlist =[i//2 for i in mylist25 if i%2==0]
print(newlist)

mylist27 = ["venke","guru","venkat","amma"] # filter the words in the list which starts with vowel 
vowels = ["a","e","i","o","u"]
newlist = [ i for i in mylist27 if i[0] in vowels]
print(newlist)


#to print the number only less than 20 using list compensation 

mylist28 = [90,21,19.9,20,21,19,15,7,9]
newlist=[]
newlist= [ i for i in mylist28 if i < 20]
print(newlist)

mylist29 = ["venkat","guru","venke"] # Converting the value to upper using list compensastion 
newlist=[]
newlist=[ i.upper() for i in mylist29]
print(newlist)


#! SORTING OF THE LISTS 
#! POINTS TO REMEMBER ON SORTING 

#! sort()----> sort keyword usesd to sort in ascending 
#! reverse() ----> used to reverse the values 
#! sort(reverse=True)  ---> used to get the value in Descending order 
#! key ---> used to sepcify a custom function which will be called on each element in the list 

mylist30 = [10,89,20,50,40]   #Sortig the value of the lists( Ascending Order )
newlist=sorted(mylist30)
print(newlist)

mylist31=[10,20,5,60] #Sort the values in Descending Order 
mylist31.sort(reverse=True)
print(mylist31)

def myfunc(n):    #! Customize Sort Function
    return (n+100)

mylist32 = [ 10,50,120,100,150]
mylist32.sort(key=myfunc)
print(mylist32)


mylist33 = ["venke","Venke","guru","GURU"]
mylist33.sort()
print(mylist33) #NOTE: case insenstive sorting 


#!HOW sorting works in Strings ?

#! sorting in strings happens based on the Unicode values of the letters , each word has a unicode value

mylist34 = ["venke","guru","venke"]
mylist34.sort()
print(mylist34)

#!COPY LISTS 

#! There are two methods to copy the values in the list 
#! copy() ---> built in methos copies the value of the list 
#! deepcopy() ----> copy the values 
#! list()  ----> Build in method used to value of one list to another list ()

#! There are two methods to copy the values in the list 


originallist = ["venke","guru","venke"]
newlist = originallist.copy()
newlist[0] = ["XXX"]
print(originallist)


mylist35 = [ 1,2,3,4,5]
mylist36=  list(mylist35)
mylist36[1]=10
print(mylist36)


#! JOIN TWO LISTS 

#! 1 . concentate the list togther 
#! 2 . append () method used to add the value to the end of the list 
#! 3 . Extend () method used to join the valies in the list 

mylist37 = ["venke","guru"]  #append to join two of the lists 
mylist38= "GURU","VENKAT"
newlist = mylist37.append(mylist38)
newlist=mylist37
print(newlist)



#we are having two values of list and need to be combined togther usning append methosd 
#the list a shoudl be joined after the llist B value 

lista = [1,2,3]
listb = [4,5,6]
for i in lista:
    listb.append(i)
print(listb)    


lista = [10,20,30,40]
listb = [50,60,70,80] #using extend () to join the two lists 


lista.extend(listb)

print(lista)
    

#! METHOS USED IN LISTS 

# append()  Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()  Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()  Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()  Removes the item with the specified value
# reverse() Reverses the order of the list
# sort()	Sorts the list











    
    

    











