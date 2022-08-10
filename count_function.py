def count_vowels(s):
    vowels = 0
    for i in s:
        if i in 'aeiou':
            vowels += 1
            print(vowels)

word = 'vowels'
count_vowels(word)
