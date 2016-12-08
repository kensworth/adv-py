prices = [1, 5, 8, 9, 10, 17, 17, 20]
size = len(prices)

def cut_rod(prices, n):
    val = [0 for _ in range(n + 1)]
    val[0] = 0
    for i in range(1, n + 1):
        max_val = 0
        for j in range(i):
            max_val = max(max_val, prices[j] + val[i - j - 1])
        val[i] = max_val
    return val[n]

print cut_rod(prices, size)
