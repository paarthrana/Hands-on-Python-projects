print("===== SIMPLE CALCULATOR =====")

while True:
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")

    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")

    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")

    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")

    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 5.")