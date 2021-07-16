try:
    no1 = int(input("1st Integer No :"))
    no2 = int(input("2nd Integer No :"))
    print("Sum = ",no1+no2)
    try:
        print("Div = ",no1/no2)
    except ZeroDivisionError as zde:
        print("Can't Divide By Zero")
    print("Sub = ", no1 - no2)
    print("Mul = ", no1 * no2)
except ValueError as ve:
    print("Only Integer Values are allowed")
print("Thanks")