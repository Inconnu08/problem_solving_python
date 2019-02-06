def reverse_vowels(s):
    s = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    start = 0
    end = len(s) - 1

    while start <= end:
        if s[start] in vowels and s[end] in vowels:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        elif s[start] in vowels and s[end] not in vowels:
            end -= 1
        else:
            start += 1

    return ''.join(s)


print(reverse_vowels('apple'))
print(reverse_vowels('hoomaan'))
