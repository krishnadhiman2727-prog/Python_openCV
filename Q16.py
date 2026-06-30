# Take a single lowercase alphabet character
letter = input("Enter the letter: ")

# The ASCII value difference between uppercase and lowercase letters is exactly 32
ascii_value = ord(letter)
uppercase_ascii = ascii_value - 32
uppercase_letter = chr(uppercase_ascii)

print(uppercase_letter)