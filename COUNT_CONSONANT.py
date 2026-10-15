#Program to count the number of consonants in a given string
def count_consonants(text):
    vowels = "aeiouAEIOU"
    consonant_count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    return consonant_count

text_1 = input("Enter a string: ")
print(count_consonants(text_1)) 