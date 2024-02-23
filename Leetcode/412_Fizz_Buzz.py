n = int(input())
output_data = []
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        output_data.append("FizzBuzz")
    elif i % 3 == 0:
        output_data.append("Fizz")
    elif i % 5 == 0:
        output_data.append("Buzz")
    else:
        output_data.append(str(i))
print(output_data)
