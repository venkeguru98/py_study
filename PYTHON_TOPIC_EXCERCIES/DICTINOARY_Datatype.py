# DICTINORAY DATATYPE 

#! KEY POINTS IN DICT DATATYPE

# dict dataype are ordered , chnagable and do not allow duplicate 
# dict are accessed by key and value 
# dict for the value any datatype can be used 
# dict datatype is mutable
# dict datatype are enclosed with curl bracklets 
# Dict datatype syntax : key : value 


#sample dict format 
thedict = {
    "name" : "venke",
    "age" : 26,
    "address" : "singapore"
    }
print(thedict)

#len of the dict 
print(len(thedict))

#type of the value
print(type(thedict))

#another way of decalring the dict datatype is by dict constructor

thedict2 = dict(name = "venke",age = 26,address = "singapoare")
print(thedict2)

#! Aceessing the value of the Dict 

#methods used for accessing the value of dict -- > 
#---> key() - gives the keys used in the dict
#---> value() - gives the values used in the dict 
#---> items() - gives the pairs of key and value used in the dict 
#----? if () and in - to check wheather the key present in the dict

# 1) can be accessed by the reffering to the key value inside the square brace 

#syntax : dictname["keyvalue"]

print(thedict["name"])
print(thedict["age"])

#2) the other way of accessing the dict is by GET() method 

#syntax : dictname.get(key)
student = {
    "name" : "xxx",
    "school" :"yyy",
    "phoneno": 12345
    
}
print(student.get("name"))
print(student.get("phoneno"))

#GET KEYS 

#key() method will return the list of keys used in the dictinoary 

x = student.keys()
print(x)

# Changing the key value and again checking the value of the key 

student["group"] = "zzz"

x = student.keys()
print(x)

# GET VALUES

# the values() method used to get the values in the dict 

print(student.values())

#changing the value of again adding a value and checking it 

student["school"] = "kvs"
print(student.values())


# GET ITEMS 

print(student.items())

student["address"] = "chennai"  ----#adding a key and value

print(student.items())

#check whether the key present in the declared dict 

if "address" in student:
    print("yes")
else :
    print("no")
    
#! CHANGE ITEMS IN THE DICT 
# update() method is used to chnange the value in the dict , will update the items in the given argument 
# Items in the dict can be chnaged by acccesing the key name 

newdict = {
    "year":2020,
    "DOB":"14nov",
    "name":"shubham"
}

newdict["year"] = 2021 #------> updating the dict 
newdict.update({"year:2021"}) #---> update method used to update the value in the dict 
print(newdict)

#! ADDING ITEMS TO THE DICTINORY 

# adding items in the dict by creating a new key with value 
# adding a item to the dict with the update method 

dict1 = dict(name ="venke",age = 26, Number = 9865254571)
dict1["name2"] = "VENKAT" #---> adding a new element by adding a new key with value 
dict1["name"] = "VENKE"
print(dict1) 


dict2 = {"name":"venke","secondname":"venkat","mobile":8667498912}
print(dict2)
dict2.update({"name":"VENKAT"})
dict2.update({"address":"singapore"})
print(dict2)

#! REMOVE DICT ITEMS 
# Removing the Dictionary items methods are 
# pop() method - pop(key) ---> removes the item with the specified key 
# popitem() --> removes the last inserted item randomly 
# del() ---> deles the specific key and also delets tne entire dict 
# clear() --- EMPTIES all the value in the dictinoary 


#pop() method 
dicttoremove = dict(name="venke",age = 40)
dicttoremove.pop("age")
print(dicttoremove)

#popitem()

dictitem = {"name":"venkat","name2":"venkat2","name3":"venkat3"}
dictitem.popitem()
print(dictitem)


#! LOOPS IN DICTINOARY : 

# looping in a dictinory using the for Loop 
# while looping through the dict , the return values are the key of the Dictonary , 
# There are some of the methods to Return the dict 

# To print the key values in the dict 

loopdict = {
    "Name" : ["venkat","guru","venke"],
    "Age" : 67
    "phone" : +91
    
}

for value in loopdict :
    print(value)

# To print the values in the dict 

print (loopdict[value])

# To print the keys and values by giving the methods - key () and value  ()

for value in loopdict.keys() : 
for value in loopdict.values():
for value in loopdict.items() #--> to print the items ( both values and key use the items() method )

#! COPYING A DICTIONARY : 

# copying a dict cannot be simply done by dict 1 = dict 2 
# copying a dict can be done by the build in methods --- > copy () and dict ()

dict1 = { 
         
         "name" :["venke","venke","venke"],
         "second name" :["venkat","venkat","venkat"],
         "phone": 78 
         
         }

print(dict1)
dict2 = dict1.copy()
print(dict 2)


# another way of copying the dictionary 

dict2 = dict(dict1)
print(dict2)

#! NESTED DICTIONARY - should continue with NESTED dict 21 / 05 / 2023 

# Dict within the dict which forms the nested dictionary 


person_dict = {
    "person1 " :{
        "name" : "venke",
        "age" : 23
    },
    "person2" : {
        "name" : "venkat",
        "age" : 20
    },
    "person3" : {
        "name":"venkat",
        "age" : 90
    }
    
} 

print(person_dict)

#Accessing the Nested Dict 

print(person_dict["person2"]["name"]])

#Another way of creating a nested Dict

person1 = {
    "name" :"venke",
    "age" : 25
}
person2 = {
    "name":"venkat",
    "age" : 26
}
person3 = {
    "name":"venkat",
    "age" : 27
}
person_dict = {
    "person1" : person1,
    "person2" : person2,
    "person3" : person3
}

print(person_dict)


#! METHODS USED IN DICT 

#clear() - remove all the elements from the dict 
 
clear_dict = (dict (name = "venke", age =23 , phone= 98652))
print(clear_dict)

clear_dict.clear()
print(clear_dict)

# fromkeys () - returns a dict with specific key and value 
# Synatx : dict.fromkeys(x,y) x - keys y - values 

x = ("value2","value1")
y = (23,'value1')

dict = dict.fromkeys(x,y)
print(dict)

# get() return the value of the specified key given 

# returs th default value none if the given key is not there 

get_item = {
    
    "name"  : "venke",
    "age"   : 23,
    "school": "XXX"
    
}

x = get_item.get("name",23)
print(x)
 
# items () -  retunrs the pair of keys and the items 
# keys () - retuns the keys of the  dict 
# value () - returns th coressponing value to the key  

items_dict = {
    
    "name" : "xxx",
    "age " : "yyy",
    "date" : 14/11/1998
    
}

item_dict1 = items_dict.items()
print(item_dict1)


# POP () METHODS removs the item with the particaluar key 

items_dict.pop("age")

print(items_dict)

#popitem() method removes the last inserted item 

items_dict.popitem()
print(items_dict)


#setdefault() returns the value of the specified key
# if the key does not exists , insert the key , with the specified value 

#syntax : dict.setdefault(keys,value)

set_dict = {
    "name"  : "venke",
    "age"  : 23,
    "fullname" : "venkatesa Guru"
}

x =set_dict.setdefault("fullname")
print(x)

#update() method used to update the value with the specified key - values 


set_dict.update({"lastname" : "s"})
print(set_dict)









