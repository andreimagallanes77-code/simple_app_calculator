def add(number_one, number_two):
    return number_one + number_two

def subtract(number_one, number_two):
    return number_one - number_two

def multiply(number_one, number_two):
    return number_one * number_two

def divide(number_one, number_two):
    return number_one / number_two

def main():
    while True:
        try:
            print("\nChoose operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            choice = input("Enter choice (1-4): ")

            number_one = float(input("Enter first number: "))
            number_two = float(input("Enter second number: "))

            if choice == "1":
                result = add(number_one, number_two)
                print("Result:", result)

            elif choice == "2":
                result = subtract(number_one, number_two)
                print("Result:", result)

            elif choice == "3":
                result = multiply(number_one, number_two)
                print("Result:", result)

            elif choice == "4":
                result = divide(number_one, number_two)
                print("Result:", result)

            else:
                print("Invalid choice!")
