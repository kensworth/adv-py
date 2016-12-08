str = '121012'
def num_decodings(s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        num_ways = [0 for x in range(len(s)+1)]
        num_ways[0] = 1
        for i in xrange(1, len(s)+1):
            if s[i-1] != '0':
                num_ways[i] += num_ways[i-1]
            if i != 1 and s[i-2:i] > '09' and s[i-2:i] < '27':
                num_ways[i] += num_ways[i-2]
        return num_ways[len(s)]

print num_decodings(str)
