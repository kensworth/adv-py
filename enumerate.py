array = ['foo', 'bar', 'baz']

for i, word in enumerate(array):
    print 'index', i
    print 'word', word

pairs = [(i, word) for i, word in enumerate(array)]
print pairs
