def f(n):
    if n > 0:
        return g(n-1) + 1
    else:
        return 0

def g(n):
    if n > 0:
        return f(n-1) + 1
    else:
        return 0

print(f(5))
print(g(10))
