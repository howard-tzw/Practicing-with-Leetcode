# https://ithelp.ithome.com.tw/articles/10281811


print([1 for _ in range(10)])
print([1] * 10)

# Fibonacci Sequence


def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(8))


def fibonacci2(n):
    if n == 0 or n == 1:
        return n
    seq = [0 for _ in range(n + 1)]
    seq[0] = 0
    seq[1] = 1
    for i in range(2, n+1):
        seq[i] = seq[i-1] + seq[i-2]
    return seq[n]


print(fibonacci2(8))


def fibonacci3(n):
    if n == 0 or n == 1:
        return n
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return b


print(fibonacci3(8))
