decimal_num = int(input("Enter your number: "))
binary_num = bin(decimal_num)
print(binary_num)

str = input("Enter you str:")
rev = ""

for i in range(len(str)-1, -1, -1):
    rev += str[i]

print("rev str is this: ", rev)
if str == rev:
    print("it's palindrome")
else:
    print("it's not palindrome")


