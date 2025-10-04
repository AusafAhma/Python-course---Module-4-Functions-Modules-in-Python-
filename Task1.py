def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

sample_number = int(input("enter the number:"))
print(f"The factorial of {sample_number} is: ")
