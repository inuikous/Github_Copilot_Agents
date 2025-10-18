class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            self.history.append("Division by zero error")
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def get_history(self):
        return self.history

if __name__ == "__main__":
    calc = Calculator()
    print("Simple Calculator\n")
    while True:
        print("Options:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "6":
            print("Goodbye!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print("Result:", calc.add(num1, num2))
                elif choice == "2":
                    print("Result:", calc.subtract(num1, num2))
                elif choice == "3":
                    print("Result:", calc.multiply(num1, num2))
                elif choice == "4":
                    print("Result:", calc.divide(num1, num2))
            except ValueError as e:
                print("Error:", e)
        elif choice == "5":
            print("History:")
            for record in calc.get_history():
                print(record)
        else:
            print("Invalid option. Please try again.")