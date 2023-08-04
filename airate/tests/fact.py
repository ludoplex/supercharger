def recursive_factorial(n):
    return 1 if n == 0 else n * recursive_factorial(n)

# Example usage
n = 5
result = recursive_factorial(n)
print(f"The factorial of {n} is {result}")
