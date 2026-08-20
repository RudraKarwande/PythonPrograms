operator = (input("Enter karo operator"))
x=2
y=5

match operator:
    case '+':             #addtion
        result= x + y
    case '-':             #subtraction
        result = x - y
    case '*':             #multiplication
        result =  x * y
    case '/':             #division
        result = x / y
    case '%':             #modulus 
        result = x % y
    case '//':             #floor division
        result = x // y

print (result)
