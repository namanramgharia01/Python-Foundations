#Program to count the number of vowels in a string
def vowel_text(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
    return vowel_count

text_1 = input("Enter a string: ")
print(vowel_text(text_1))