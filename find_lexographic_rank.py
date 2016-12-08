def find_lexographic_rank(rem, res):
    if not rem:
        perms.append(res)
        print res
        if res == string:
            return len(perms) % 1000003
    for i in xrange(len(rem)):
        rank = find_lexographic_rank(rem[:i] + rem[i+1:], res+rem[i])
        if rank:
            return rank

string = 'facebook'
perms= []
print find_lexographic_rank(sorted(string), '')

