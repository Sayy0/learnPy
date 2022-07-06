import math

print("\n=========================")
print("\n (0) Cancel Operation")
print("\n (1) + ")
print("\n (2) - ")
print("\n (3) x ")
print("\n (4) / ")

operation = -1

while operation < 0 or operation > 4 or math.isnan(operation):
    try:
        operation = int(input("\nChoose Operation : "))
    except:
        print("\nPlease enter a valid selection!!\n")

if operation == 0:
    print("\nCancelled Operation, exiting program.\n")
    exit()
else:
    num1 = int(input("Num 1 : "))
    num2 = int(input("Num 2 : "))

    if operation == 1:
        answer = num1 + num2
        symbol = '+'
    elif operation == 2:
        answer = num1 - num2
        symbol = '-'
    elif operation == 3:
        answer = num1 * num2
        symbol = 'x'
    else:
        answer = num1 / num2
        symbol = '/'

    print("\n=======================================")
    print("Answer: " , num1, " ", symbol, " ", num2, " = ", answer)
