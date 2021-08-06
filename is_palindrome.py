input_word = input("Please enter the string to chk for palindrome : ")

palindrome_list = []

for ch in input_word:
	palindrome_list.append(ch)

# print(palindrome_list)

#check if palindrome or not

if palindrome_list == palindrome_list[-1::]:
	print("it is palindrome")
else:
	print("not a palindrome")

