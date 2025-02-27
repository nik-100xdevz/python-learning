def is_vowel(char):
    """Returns True if the character is a vowel, False otherwise."""
    return char.lower() in 'aeiou'

# Taking input from user
char = input("Enter a character: ")

# Ensuring the input is a single character
if len(char) == 1 and char.isalpha():
    print(is_vowel(char))
else:
    print("Please enter a single alphabet character.")