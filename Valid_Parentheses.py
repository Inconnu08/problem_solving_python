def isValid(s: str):
    tokens = list(s)
    l1 = 0
    l2 = 0
    l3 = 0

    for t in tokens:
        if t == '(':
            l1 += 1
            continue
        if t == '{':
            l2 += 1
            continue
        if t == '[':
            l3 += 1
            continue
        if t == ')':
            l1 -= 1
            continue
        if t == '}':
            l2 -= 1
            continue
        if t == ']':
            l3 -= 1

    return (abs(l1) + abs(l2) + abs(l3)) == 0


print(isValid("{[()]}()"))
print(isValid("([)]"))


def isValidSimple(s: str):
    tokens = list(s)
    left = 0

    for t in tokens:
        if t == '(':
            left += 1
        else:
            left -= 1

    return left == 0


print(isValidSimple("(())()"))


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []


def isValidReal(s: str) -> bool:
    tokens = {"(": ")", "[": "]", "{": "}"}
    curstack = Stack()
    for c in s:
        if c in tokens:
            curstack.push(c)
        elif curstack.is_empty() or c != tokens[curstack.pop()]:
            return False
    return curstack.is_empty()


print(isValidReal("{[()]}()"))

