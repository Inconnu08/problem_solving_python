from itertools import islice


def is_valid(string: str) -> bool:
    tokens = {'a': 'bc'}
    stack = []
    iter_s = iter(enumerate(string))

    for i, s in iter_s:
        if s in tokens:
            stack.append(s)
        else:
            if not stack:
                return False
            try:
                a = s + string[i + 1]
                next(islice(iter_s, 2), None)
            except IndexError:
                return False
            if a != tokens[stack.pop()]:
                return False
    return stack == []


def isValid(S: str) -> bool:
    stack = []
    for s in S:
        if s == "c" and len(stack) >= 2:
            if stack[-2:] == ["a", "b"]:
                stack = stack[:-2]
        else:
            stack.append(s)
    return stack == []


print(is_valid("aabcbc"))
print(is_valid("abcabcababcc"))
print(is_valid("abccba"))
print(is_valid("cababc"))
print()
print(isValid("aabcbc"))
print(isValid("abcabcababcc"))
print(isValid("abccba"))
print(isValid("cababc"))

s = [1, 2, 3, 4, 5, 6, 7]
print(s[-2:])
print(s[:-2])
