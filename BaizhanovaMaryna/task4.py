letter = input(("Enter a letter: "))

if str(letter)[::-1] == str(letter):
    print("Word:", letter, " is a Palindrome")
else:
    print("Word:", letter, " is not a Palindrome")