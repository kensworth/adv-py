arr = [1,2,3,4,5,5,6,6]
dictionary = {}
for num in arr:
    dictionary[num] = dictionary.get(num, 0) + 1

print dictionary


