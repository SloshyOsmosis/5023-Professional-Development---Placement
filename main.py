user = input("Please enter a palindrome: ")
palinword = user.lower()

def ispalindrome(palinword):
    return palinword == palinword[::-1]

answer = ispalindrome(palinword)

if answer:
    print("This word is a palindrome")
else:
    print("This is not a palindrome")