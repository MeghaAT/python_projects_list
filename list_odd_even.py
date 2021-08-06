a = [1, 11, 40, 55, 100]

odd = []
even = []
#print both odd and even
for num in a:
	if num%2 == 0:
		even.append(num)
	else:
		odd.append(num)

print(f"Odd numbers are {odd}")
print(f"Even numbers are {even}")

