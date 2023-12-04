# def decToBinary(num, exp):
#     if num == 1:
#         return 10**exp
#     else:    
#         return (num%2 * 10**exp) + decToBinary(num//2,exp+1)

# print(decToBinary(int(input()),0))

def decToBinary(n):
    assert int(n) == n, 'Number should be integer'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decToBinary(n//2)

print(decToBinary(int(float(input()))))
