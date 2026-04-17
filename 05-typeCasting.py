#Type casting মানে হলো এক data type থেকে অন্য data type-এ convert করা।

# string -> int
num = "1254566"
a = int(num)
print(a)
print(type(a))

# string -> float
num1 = "50"
b = float(num1)
print(b)
print(type(b))

#
price = float(input("product price is:"))
quantity = int(input("product quantity is:"))
totalPrice = price * quantity
print("Total cast is", totalPrice)

#
birthYear = int(input("birth year is:"))
currentYear = 2026
age = currentYear - birthYear

print(age)

#
math = int(input("math mark is:"))
eng = int(input("english mark is:"))
phy = int(input("phy mark is:"))
che = int(input("che mark is:"))
total = math + eng + phy + che
percentage = total / 4
print("percentage ", percentage)

#
attemt = int(input("enter number of attemt is:"))
if attemt >= 3:
    print("account locked")
else:
    print("try again")