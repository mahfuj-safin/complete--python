student = ("safin", 1, "CST")
print("Name:", student[0])
print("Roll:", student[1])
print("Department:", student[2])



product = ("Laptop", 50000, 5)
name, price, stock = product
print("Name:", name)
print("Price:", price)
print("Stock:", stock)


students = [
    ("safin", 80),
    ("Rahim", 50),
    ("karim", 64)
]
for s in students:
    print("Name:", s[0], "| marks:", s[1])


topper = [
    ("safin", 80),
    ("Rahim", 50),
    ("karim", 64)
]
topper = max(topper, key = lambda x: x[1])
print(topper)


menu = [
    ("barger", 150),
    ("pizza", 200),
    ("chicken", 300)
]
for item in menu:

    print("Name:", item[0], " : Price:", item[1])
