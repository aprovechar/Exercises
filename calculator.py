# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# result = float(num1) + float(num2)
# print(res)

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
choice = int(input("Enter your choice: "))
if 1 <= choice <= 4:
    print("Enter two numbers: ")
    num1 = int(input())
    num2 = int(input())
    if choice == 1:
        res = num1 + num2
        print(res)
    elif choice == 2:
        res = num1 - num2
        print(res)
    elif choice == 3:
        res = num1 * num2
        print(res)
    else:
        res = num1 / num2
        print(res)
elif choice == 5:
    exit()
else:
    print("Error! Wrong input..!!")
