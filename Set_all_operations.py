
fruit_set = {"apple","muskmelon","banana","GRAPES"}
print (fruit_set)

# Add function in set 
fruit_set = {"apple","muskmelon","banana","GRAPES"}
fruit_set.add("mango")
print (fruit_set)

#Update function in set
fruit_set = {"apple","muskmelon","banana","GRAPES"}
fruit_set.update(["mango","kiwi"])
print (fruit_set)

#Remove function in set 
fruit_set = {"apple","muskmelon","banana","GRAPES"}
fruit_set.remove("GRAPES")
print(fruit_set)

#Union function 
Set_1 = {1,2,3,4,5,6.7}
set_2 = {8,58,23,556,8985}
set_3 = Set_1.union(set_2)
print (set_3)
print (Set_1 | set_2)

#Intersection function
Set_1 = {1,2,3,4,5,6.7}
set_2 = {8,58,23,556,8985}
Set_3 = (Set_1).intersection (set_2)
Set_3 = (set_2).intersection (Set_1)
print (Set_3)
print (Set_1 & set_2)

#Diffrence Function
Set_1 = {'a','b','c','d'}
Set_2 = {1,2,3,5}
set_3 = Set_1.difference(Set_2)
print(set_3)
set_3 = Set_2.difference(Set_1)
print(set_3)


