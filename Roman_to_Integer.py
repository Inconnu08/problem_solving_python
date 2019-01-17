romans = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

s = "MCMXCIV"

r, i = 0, 0

while i < len(s):
    try:
        r += romans[s[i] + s[i+1]]
        i += 2
    except(IndexError, KeyError):
        r += romans[s[i]]
        i += 1
print(r)
