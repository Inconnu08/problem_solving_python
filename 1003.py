def isValid(s: str) -> bool:
    stack = []

    for token in s:
        stack.append(token)
        if len(stack) >= 3 and stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
            stack.pop()
            stack.pop()
            stack.pop()

    return stack == []

print(isValid('aabcbc'))
print(isValid('abcabcababcc'))
print(isValid('abccba'))
print(isValid('cababc'))
