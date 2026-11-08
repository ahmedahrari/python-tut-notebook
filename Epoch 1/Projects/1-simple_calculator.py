print("====== SIMPLE CALCULATOR ======")

num1 = float(input("NUM1: "))
num2 = float(input("NUM2: "))
operator = input("Operator (+, -, *, /, %, **, //): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Divide Not allowed"
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
elif operator == "//":
    result = num1 // num2
else:
    result = "Operator is Invaild !!"

print(f"Result: {num1} {operator} {num2} = {result}")