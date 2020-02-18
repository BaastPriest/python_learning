import math
std_1 = int(input())
std_2 = int(input())
std_3 = int(input())

des_1 = math.ceil(std_1 / 2)
des_2 = math.ceil(std_2 / 2)
des_3 = math.ceil(std_3 / 2)

all_des = des_1 + des_2 + des_3

print(all_des)