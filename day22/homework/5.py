run = int(input("enter your number: "))

sum = 1

for i in range(1, run + 1):
    sum += sum * i

print(sum)