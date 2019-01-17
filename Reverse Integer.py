def reverse_number(n):
    r = 0

    while n > 0:
        r *= 10
        r += n % 10
        n //= 10

    return r


def reverse_number_2(n):
    # print(int(str(213)[::-1]))
    if n > 1073741824:
        return 0

    n = str(n)

    if n[0] == '-':
        return int('-' + n[:0:-1])
    else:
        return int(n[::-1])


print(reverse_number(120))

print(reverse_number_2(-423))

print(reverse_number_2(1534236469))
