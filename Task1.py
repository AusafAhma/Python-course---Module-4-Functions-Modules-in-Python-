def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result
def factorial_recursive(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial_recursive(x - 1)

n = int(input("Enter a number: "))

print("Factorial of 5 is:", factorial_recursive(n))
