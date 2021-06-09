def primeLoop(i):
    lst = []
    n = i
    for x in range(1, i * 2, 2):
        lst.append(x)
    while n:
        for k in lst:
            print(k, end="")
        lst.append(lst.pop(0))
        n -= 1
        print()


n = int(input("Enter number : "))
primeLoop(n)
