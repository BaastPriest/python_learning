a = int(input())
b = int(input())
c = int(input())
min_num = int()

if a < b:
    min_num = a
else:
    min_num = b
if min_num > c:
    min_num = c

print(min_num)