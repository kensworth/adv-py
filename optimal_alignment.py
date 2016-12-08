string = 'I am a big fan of rats'
min_cost = float('inf')

def align_text(L, string, cost_so_far):
    global min_cost
    string = string.strip()
    if L >= len(string):
        cost_so_far += (L - len(string)) ** 3
        if cost_so_far < min_cost:
            min_cost = cost_so_far
        return
    word_ends = []
    for i in range(L):
        if string[i] == ' ':
            word_ends.append(i)
    if string[L] == ' ':
        word_ends.append(L)
    for word_end in word_ends:
        cost = cost_so_far + (L - word_end) ** 3
        align_text(L, string[word_end:], cost)
    return min_cost

print align_text(10, string, 0)
