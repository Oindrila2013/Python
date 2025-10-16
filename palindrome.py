def ispalindrome(string):
    left_pos = 0
    right_pos = len(string) -1
    while right_pos <= left_pos:
        if not string[right_pos] == string[left_pos]:
            return False
        left_pos +=1
        right_pos -=1
    return True

print("Is this a palindrome string ?")
print(ispalindrome("malaylam"))
        