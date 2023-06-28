#! SETS in Python 

#! Sets are unchangable , unindexed , unorderd 
#! Sets do not allow for duplicate values
#! Sets are enclosed withn the closed brackets 
#! Setss cannot be accessed by index values or key valuaes
#! In sets True and value 1 are same so dont allow for duplicate

#---------

#! Acesing the elements in SET 

#! Access the elements in SETs can be by loops and by checking the condition ( using in )

    # set1 = {"venke",1,2}
    # for setvalue in set1:
    #     print(set1[setvalue]) #---->This throws the error as sets are not orderable (set objects is not subscripatble)

set1 = {1,10,20,"venke"}
for i in range(len(set1)):
    print(i)
    
    
set1 ={10,20,"venke",30}
print(30 and 10 in set1)

#! ADD SET ITEMS 

#! once a set is created its Existing set value cannot be changed but the new value can nbe added 

set_value = {1,2,3,4,"one","two"}
set_value.add("three")
print(set_value)   # -----> This adds the new value to the set witout chnage in any of the values 

#! To add the current set to another set use update () method 

set_value1 = {1,2,3,4,5}
set_value2 ={"venke","guru","venkat"}
set_value1.update(set_value2)

print(set_value1)

#! any literables can be aded with sets ( eg : sets can be aded with other datatypes like tuples, list)

set = {1,2,3,4,5}
list = [ 1,2,3,4,5]
set.update(list)
print(set) #-------------> In this output set wont allow for duplicate values 


#! REMOVE THE ITEMS AND REMOVE THE SET 
#Methods used for removing the items 
#remove() - to remove a item in the set and if the item does not exits it puts a error 
#discard() - to remove a item in the set and if the item does not exists also it doesnt put a error 
#pop() -randomly removes any item in the set as sets are unordered 
#clear()  clears all the elements in the set 
#del() - deetes the complete set 

setvalue = {"venke",1,"guru"}
setvalue.remove(1)
print(setvalue) #-----------> removes the value 1 

setvalue = {"venke",1,"guru"}
setvalue.remove("GURU")
print(setvalue) #------------> Throws an error as the item doesnt exists

setvalue = {"venke",1,"guru"}
setvalue.discard("GURU") 
print(setvalue) #------------> doesnt put error in output , prints the original value 

setvalue = {"venke",1,"guru"}
setvalue.pop("GURU") #----------- > pop method doesnt get any arguments in it , outputs error 
print(setvalue)

setvalue = {"venke",1,"guru"}
setvalue.clear() 
print(setvalue) #----------> clears the entire set value 

setvalue = {"venke",1,"guru"}
del setvalue
print(setvalue) #-----------> Removes even the memory alocated for the variable 


#! LOOP SETS 

# for Loops 

setvalue = { "venke","venkat","guru"}

for value in setvalue:
    print(value)
    
#! JOINS IN SETS 

# update() - inserts the item with one to another 
# union () - combines the two sets and returns with a new set

# NOTE : Both union() and update() will exclude the duplicate items 

# intersection_update() - will keep only the item in both the sets 
# intersection() - returns a new set that contains the same item in the sets 

# symmentrical_difference_update() - return the unncommon items in the sets
# symmentrical_difference() - returns a new set that contains only the uncommon items in the sets 

#update
setvalue1 = {"venkat","guru","venkat"}
setvalue2 = {"venke","GURU","venkat"}

setvalue1.update(setvalue2)
print(setvalue1)

#Intersection_update
val1 = {"venke","venkat","GURU","guru"}
val2 = {"guru",1,2}

val1.intersection_update(val2)
print(val1)

#issubset method to check if set1 is a subset of set2. 
#The method returns True if all elements of set1 are present in set2, and False


#! SET METHOS 

# add()	        Adds an element to the set
# clear()	    Removes all the elements from the set
# copy()	    Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	    Remove the specified item
# intersection()Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	        Removes an element from the set
# remove()	    Removes the specified element
# symmetric_difference()Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	    Return a set containing the union of sets
# update()	    Update the set with the union of this set and others






