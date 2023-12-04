def flatten(arr):
    res =[]
    for ele in arr:
        if type(ele) is int:
            res.append(ele)
        elif type(ele) is list:
            res = res + flatten(ele)
    return res

print(flatten([1,[2,[3,4],[[5]]]]))
#print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]))
print(flatten([[1],[2],3]))