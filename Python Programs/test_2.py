for i in range(1, int(input())+1):
    print(((10**i)//9)**2)

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(i * int((10 ** i - 1) / 9))
