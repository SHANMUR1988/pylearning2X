# Print the multiples of a integer
# of a number upto 10

num = int(input("Enter the number\n"))

print("Multiplication Table of", num)
for i in range(1,11):
    print(num, '*', i , "=", num * i)

