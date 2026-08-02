#perform all list operations in python:
# 1.empty list operations
list = []
print(list)

#print list wth string and number elements
family = [7,9,29,"Ravindra","Renuka","Rudra",'R']
print(family)

#2.Append function 
family = [7,9,29,"Ravindra","Renuka","Rudra",'R']
family.append("Hostel members")
print(family)

#3. Extend function
family = [7,9,29,"Ravindra","Renuka","Rudra",'R']
family.extend( ["Nikhil","Samrudhhi","Pranil",2025])
print (family)

 #4. Insert functin
family =[7,9,29,"Ravindra","Renuka","Rudra",'R']
family.insert(5,"Nikhil")
print(family)

#5.Delete function(single element) by index value concept
family =[7,9,29,"Ravindra","Renuka","Rudra",'R']
del family[6]
print(family)

#6. delete function by index range
family = [7,9,29,"Ravindra","Renuka","Rudra",'R']
del family[1:4]
print (family)

#7. Complete delete
family =[7,9,29,"Ravindra","Renuka","Rudra",'R']
del family

#8.reverse function
family = [7,9,29,"Ravindra","Renuka","Rudra",'R',"Nikhil","Samruddhi","Pranil"]
family.reverse()
print(family)


