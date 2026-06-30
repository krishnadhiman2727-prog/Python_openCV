# Take a string input from the user
text = input("Enter a string: ")
print("You entered:", text)

vowel_count = 0
vowels = "aeiouAEIOU"

# Iterate and count vowels
for char in text:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)