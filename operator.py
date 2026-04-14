# python operator
# python a 8 type operator royeche

"""
1. Arithmetic
2. Comparison
3. Logical Operators
4. Assignment Operators
5. Boolean Operators
6. Membership Operators
7. Identity Operators
8. Bitwise Operators
"""

# Arithmetic Operator
a = 20
b = 30
print(a + b) # (+) addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a % b) # modulus
print(a ** b) # Exponent
print(a // b) # Floor Division

# Assignment Operators
d = 5
sum = d + 5
print(sum)

x = 10
x += 5 #ager songkhar sathe notun man add korar jonno (+=) aita use kora hoy
print(x)
x -= 2
print(x) #ager songkhar sathe notun man bad korar jonno (-=) aita use kora hoy
x *= 3
print(x)
y = 5
y **= 2
print(y)
z = 10
z /= 2
print(z)
e = 20
e %= 2
print(e)
f = 13
f //= 2
print(f)

# Comparison Operator
g = 5
h = 10
print(g == h) # equal
print(g != h) # not equal
print(g > h) # geter than
print(g < h) #less than
print(g >= h)
print(g <= h)

# Logical Operators
i = 10
print(i > 5 and i < 9)
print(i > 5 or i < 5) # je kono akta sotto hole true dibe output
print(not(i > 5 and i < 9)) # outpur ta revese kore dey, true hole false and false hole true

#Bitwise Operators
j = 5
k = 3
print( j & k) # duita bit a 1 thakle dekhabe 1 and duitar aktay jodi kono 1 na thake tokhon dekhabe 0. and =(&)
print( j | k)
print( j ^ k)
print( ~ k)
print( j << 1)
print( j >> 1)

#Membership Operators
l = [2,5,6,7]
print(2 in l)
print(10 in l)
print(10 not in l)
m ='safin'
print('s' in m)
print('k' not in m)

#swaping
n = 50
o = 60
n,o = o,n
print('this value is now o',o )# swaping
print('this value is now n', n)
