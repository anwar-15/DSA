#To reverse a string
def reverse(string):
    if len(string) < 2:
        return string[0]
    return reverse(string[1:]) + string[0]
print(reverse('python'))    
