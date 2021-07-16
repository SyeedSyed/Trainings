try:
    no1 = int(input("1st Integer No :"))
    no2 = int(input("2nd Integer No :"))
    print("Sum = ",no1+no2)
    print("Div = ",no1/no2)
except ZeroDivisionError as zde:
    print(zde)
except ValueError as ve:
    print(ve)
print("Sub = ",no1-no2)
print("Mul = ",no1*no2)
print("Thanks")