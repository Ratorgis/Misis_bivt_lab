from string import ascii_uppercase

s = input()

first, seconde = 0, 0

for i in range(len(s)):
    if s[i] in ascii_uppercase:
        first = i
        if seconde:
            break
    elif s[i].isdigit():
        seconde = i + 1
        if first:
            break

print(s[first :: seconde - first])
