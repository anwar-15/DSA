def factorial(n):
    assert n >=0 and int(n) == n, 'factorial should be integer and positive'
    if n in [0,1]:
        return n
    else:
        return factorial(n-1) + factorial(n-2)
print(factorial(4))    