def GCD(A,B):
    assert int(A) == A and int(B) == B , 'Numbers must be integers'
    if B == 0:
        return A
    else:    
        return GCD(B,A%B)
A,B = map(int,(input().split()))
print(GCD(abs(A),abs(B)))