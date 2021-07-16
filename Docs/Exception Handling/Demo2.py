no1 = int(input("1st Integer No :"))
no2 = int(input("2nd Integer No :"))
print("Sum = ",no1+no2)
try:
    print("Div = ",no1/no2)
except ZeroDivisionError as zde:
    print(zde)
    print("Don't Divide By Zero")
print("Sub = ",no1-no2)
print("Mul = ",no1*no2)
print("Thanks")