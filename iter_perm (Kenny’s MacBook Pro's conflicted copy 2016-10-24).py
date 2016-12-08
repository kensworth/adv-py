str = 'iter'

def iter_perm(str):
    perms = []
    if not str:
        return []
    for i in range(len(str)):
        if i == 0:
            perms.append(str[i])
            continue
        new_perms = []
        for perm in perms:
            new_perms.extend(insert(str[i], perm))
        perms = new_perms
    return perms

def insert(letter, perm):
    new_list = []
    for i in range(len(perm) + 1):
        left = perm[:i]
        right = perm[i:]
        new_list.append(left + letter + right)
    return new_list

print iter_perm(str)
