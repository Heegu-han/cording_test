# for문 사용
def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a
result = factorial(1000000)
print(result)
