word = "Programming"
#Reverse

print(word[::-1])

#For first 3 and last 3

print(word[:3],word[-3:])

#For count m

print(word.count("m"))

#for palindrome

def is_palindrome(w):
    if w==w[::-1]:
        return True
    else:
        return False
print(is_palindrome("level"),is_palindrome("Python"))
