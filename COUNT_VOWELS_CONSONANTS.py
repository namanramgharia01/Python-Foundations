#program to count the number of vowels and consonants in a given string
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

text_1 = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(text_1)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)