# Python Calculator by Prince Pathak
import time
def calculator():
    print("🧮 Welcome to Prince Pathak's Python Calculator!\n")

    while True:
        try:
            num1 = float(input("🔢 Enter first number: "))
            print("'+' is addition, '-' is subtraction, '*' is multiplication, / is division, '%' is modulus, '//' is floor division, ** is exponentiation.\n")
            operator = input("➕ Choose operation (+, -, *, /, %, //, **): ")
            num2 = float(input("🔢 Enter second number: "))
            print("🔍 Performing your calculation...\n")
            time.sleep(2)  # Simulate a short delay for better user experience
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            elif operator == '%':
                result = num1 % num2
            elif operator == '//':
                result = num1 // num2
            elif operator == '**':
                result = num1 ** num2
            else:
                print("❌ Invalid operator! Try again.\n")
                continue

            print(f"✅ Result: {result}\n")

        except ZeroDivisionError:
            print("❗ Cannot divide by zero!\n")
        except ValueError:
            print("❗ Please enter valid numbers!\n")

        again = input("🔁 Wanna calculate again? (y/n): ")
        if again.lower() != 'y':
            print("\n👋 Thanks for using Prince’s Calculator. Hope you have great mindful day ahead!\n")
            break

calculator()
# End of calculator code
    