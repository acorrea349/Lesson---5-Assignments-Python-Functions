# Task 1: Create functions for each arithmetic operation.

def addition(a,b):
    return a + b
    

def subtraction(a,b):
    return a - b
    

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        raise ValueError("Cant divide by 0")
    return a / b

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.
operator = input("Tell us do you want to use an addition, subtraction, multiplication or a division: ")
num1 = float(input("Input your first number: "))
num2 = float(input("Now input your second number: "))





# Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling 
# set up to prevent an error from showing in the console.

# def calculator(a,b):
#     if operator == "addition":
#         return addition

        
#     elif operator == "subtraction":
#         return subtraction

#     elif operator == "multiplication":
#         return multiplication

#     elif operator == "division":
#         return division
        
#     else:
#             print("sorry, entry not valid.")
# calculator(num1, num2)
# print(calculator(num1,num2))



if operator == "addition":
    result = addition(num1, num2)
    print(result)

        
elif operator == "subtraction":
    result = subtraction(num1, num2)
    print(result)


elif operator == "multiplication":
    result = multiplication(num1, num2)
    print(result)


elif operator == "division":
    if num2 == 0:
        print("Cant divide by 0")
    else:
        result = division(num1, num2)
        print(result)

        
else:
    print("sorry, entry not valid.")



