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
