def factorial(n):
    return n * factorial(n-1) if n > 1 else 1

result = factorial(4)
print(result)
