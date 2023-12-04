def isPalindrome(strng):
    le = len(strng)
    if le in [0,1]:
        return True
    if strng[0] != strng[-1]:
        return False
    else:
        return isPalindrome(strng[1:le-1])

print(isPalindrome('caac'))