def count_vowels(string, vowels):
    
    string = string.casefold()

    count = {}.fromkeys(vowels, 0)

    for character in string:

        if character in count:
            count[character] += 1
    return count

vowels = "aeiou"

string = input("Please enter a word: ")

print(count_vowels(string, vowels))