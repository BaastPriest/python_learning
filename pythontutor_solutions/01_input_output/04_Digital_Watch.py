n = int(input())
h = (n // 60)
if h >= 24:
    h = (h % 24)

m = (n % 60)
print(h)
print(m)
