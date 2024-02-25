s = ["h","e","l","l","o"]

# print(s[::-1])
left, right = 0, len(s) - 1
while left < right:
    s[left], s[right] = s[right], s[left]
    left, right = left+1, right-1
