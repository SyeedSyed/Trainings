
def calc(no1,no2):
    try:
        return no1/no2
    except ZeroDivisionError:
        raise ValueError("Cannot Divide By Zero")



try:
    print("Result = ",calc(10,0))
except ValueError as ve:
    print(ve)
