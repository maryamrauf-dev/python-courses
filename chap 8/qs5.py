def meter_converter(n):
    cent=n*2.54
    return cent
inches=int(input("enter the lengeth:"))
# meter_converter(inches)
print(f"{inches} inches in centimeter is {meter_converter(inches)}")