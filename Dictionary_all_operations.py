# 1. empty dictionary declare
dict ={}
print (dict)

#2. Dictionary with string and numbers
car_dict= {"brand":"ford","model":"mustang","year":1967}
print (car_dict)

#3.length of dictionary
car_dict= {"brand":"ford","model":"mustang","year":1967}
print(len(car_dict))

#4. update dictionary
car_dict= {"brand":"ford","model":"mustang","year":1967}
car_dict.update({"owner":"rocky bhai"})
print(car_dict)

#5. loop through dictionary
car_dict= {"brand":"ford","model":"mustang","year":1967,"owner":"rocky bhai"}
for x in car_dict:
    print(x)
    
