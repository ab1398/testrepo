firstNum = int(input("First num: "))
secondNum = int(input("Second num: "))
calc = input("What do you want to do with the 2 numbers: ")

def add(x,y):
    print(f"The number is : {x+y}")

def sub(x,y):
    print(f"The number is : {x-y}")
    
def mul(x,y):
    print(f"The number is : {x*y}")
    
def div(x,y):
    print(f"The number is : {x/y}")

def mod(x,y):
    print(f"The number is : {x%y}")


if calc == '+':
    add(firstNum,secondNum)
elif calc == '-':
    sub(firstNum,secondNum)
elif calc == '*':
    mul(firstNum,secondNum)
elif calc == '/':
    div(firstNum,secondNum)
elif calc == '%':
    mod(firstNum%secondNum)
else:
    print("Wrong input")
    
    
    
# match calc:
#     case '+':
        
#         print(f"You selected add feature so the number is {firstNum+secondNum}")
#     case '-':
        
#         print(f"You selected sub feature so the number is {firstNum-secondNum}")
#     case '*':
        
#         print(f"You selected multiple feature so the number is {firstNum*secondNum}")
#     case '/':
        
#         print(f"You selected div feature so the number is {firstNum/secondNum}")
#     case '%':
        
#         print(f"You selected mod feature so the number is {firstNum%secondNum}")
#     case _:
#         print("No match")

