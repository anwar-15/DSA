def powerOfNumber(base,exp):
    assert exp >=0 and int(exp) == exp, 'exponent of the number should be positive integer'
    if exp == 0:
        return 1
    else:    

        return base * powerOfNumber(base,exp-1) 

base = input()
exp = int(input())
base = float(base) if '.' in base else int(base)
print(powerOfNumber(base,exp))