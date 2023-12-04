def capitalizeFirst(arr):
    if len(arr) == 0:
        return list()
    else:
        res = list(arr[0][0].upper() + arr[0][1:])
        return res + capitalizeFirst(arr[1:])
print(capitalizeFirst(['car','taco','banana']))        