num = int(input("enter number of digits you want in series : "))

first = 0
second = 1

print("\nfibonacci series is:")
print(first, ",",second, end=", ")

for i in range(2, num):
    next = first + second
    print(next, end=", ")

    first = second
    second = next