vowels = ['a', 'e', 'i', 'o', 'u']
three_vowels = []

def create_names(vowels, perm, num_left, three_vowels):
    if num_left == 0:
        three_vowels.append(perm)
        return
    for vowel in vowels:
        cont_perm = list(perm)
        cont_perm.append(vowel)
        create_names(vowels, cont_perm, num_left - 1, three_vowels)

create_names(vowels, [], 3, three_vowels)

for value in three_vowels:
    print value[0] + 'l' + value[1] + 'n' + value[2]
