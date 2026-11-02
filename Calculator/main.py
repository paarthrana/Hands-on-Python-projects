try:
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
except ValueError:
    print("Invalid input! Please enter numeric values.")
    exit()  
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")
choice=input("Enter choice(1/2/3/4/5): ")

try:
    if choice=='1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice=='2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice=='3':   
         print(f"{num1} * {num2} = {num1 * num2}")
    elif choice=='4':
        if num2==0:
            print("Error! Division by zero.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    elif choice=='5':
        print("Exiting the calculator. Goodbye!")
    else:
        print("Invalid input")

except Exception as e:
    print("An error occurred:", e)
