print("\n=========================")
print("\n (0) Cancel Operation)")
print("\n (1) + ")
print("\n (2) - ")
print("\n (3) x ")
print("\n (4) / ")

operation = str(input("\nChoose Operation : "))

num1 = int(input("Num 1 : "))
num2 = int(input("Num 2 : "))

match operation:
    case '1':
        answer = num1+num2
        symbol = '+'
    case '2' :
        answer = num1-num2
        symbol = '-'
    case '3' :
        answer = num1*num2
        symbol = 'x'
    case '4' :
        answer = num1/num2
        symbol = '/'

print("\n=======================================")
print("Answer: " , num1, " ", symbol, " ", num2, " = ", answer)