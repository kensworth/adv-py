def removeInvalidParentheses(s):
        open = 0
        extra_set = set()
        balanced = set()
        for i in range(len(s)):
            if s[i] == '(':
                open += 1
            elif s[i] == ')':
                if open:
                   open -= 1
                else:
                    extra_group = [i]
                    for j in range(i):
                        if s[j] == ')':
                            extra_group.append(j)
                    extra_set.add(tuple(extra_group))

        for extras in extra_set:
            balanced_string = ''
            for i in range(len(extras)):
                if i == 0:
                    balanced_string += s[:extras[i]]
                elif i == len(extras) - 1:
                    balanced_string += s[extras[i] + 1:]
                else:
                    balanced_string += s[extras[i - 1] + 1: extras[i]]
            balanced.add(balanced_string)

        print balanced

str = '()())(()'
removeInvalidParentheses(str)
