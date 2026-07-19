item1 =input("Enter the name of first item: ")
price1=float(input("Enter the price of first item: "))

item2 =input("Enter the name of second item: ")
price2=float(input("Enter the price of second item: "))

item3 =input("Enter the name of third item: ")
price3=float(input("Enter the price of third item: "))

item4 =input("Enter the name of fourth item: ")
price4=float(input("Enter the price of fourth item: "))

item5 =input("Enter the name of fifth item: ")
price5=float(input("Enter the price of fifth item: "))

Total = price1+price2+price3+price4+price5

print(item1, end=" ")
print("=",price1)
print(item2, end=" ")
print("=",price2)
print(item3, end=" ")
print("=",price3)
print(item4, end=" ")
print("=",price4)
print(item5, end=" ")
print("=",price5)

print(f"The total bill is {Total}")