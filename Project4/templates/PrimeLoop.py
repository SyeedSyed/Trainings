def primeLoop(i):
    lst = []
    n = i
    while i:
        j = 1
        j = i * 2 - j
        lst.insert(0, j)
        i -= 1
    while n:
        for k in lst:
            print(k, end="")
        lst.append(lst.pop(0))
        n -= 1
        print()


n = int(input("Enter number : "))
primeLoop(n)
