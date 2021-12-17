from art import logo

def add(n1, n2):
    """returns the summation of 2 numbers"""
    return n1+n2

def subtract(n1,n2):
    """returns the difference of 2 numbers"""
    return n1-n2

def multiply(n1,n2):
    """returns the multiplication of 2 numbers"""
    return n1*n2

def divide(n1,n2):
    """returns the division of 2 numbers"""
    return n1/n2

operations ={
      "+": add,
      "-": subtract,
      "*": multiply,
      "/": divide
    }



def calculate(num1):
    operational_symbol=input("Pick an operation: ")
    operation_function=operations[operational_symbol]
    num2 = float(input("What's the next number? : "))
    first_answer=operation_function(num1,num2)
    print(f"{num1} {operational_symbol} {num2} ={first_answer}")
    return first_answer



def calculator():
    print(logo)
    num1 = float(input("What's the first number? : "))
    for operator in operations:
        print(operator)
    first_answer=calculate(num1)    
    to_continue=input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation.:")


    while to_continue=='y':
        first_answer=calculate(first_answer)
        to_continue=input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' start a new calculation.:")
        if to_continue=='n':
            calculator()

calculator()