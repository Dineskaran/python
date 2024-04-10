def add(num1, num2):
  return num1 + num2


class Calculator:
  def subtract(self, num1, num2):
    return num1 - num2
  def multiply(self, num1, num2):
    return num1 * num2

  def divide(self, num1, num2):
    if num2 == 0:
      print("Cannot divide")
    else:
      num1/num2

calculator = Calculator()

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
  result = add(num1, num2)
elif operation == '-':
  result = calculator.subtract(num1, num2)
elif operation == '*':
  result = calculator.multiply(num1, num2)
elif operation == '/':
   result = calculator.divide(num1, num2)
else:
  result = "Invalid operation."

print("Result:", result)