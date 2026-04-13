# data type

#python a data type 4 dhoroner hoye thake

"""
1. Number
2. String
3. boolean
4. binary
5. none type data
6. List
7. tuple
8. range
"""
from enum import nonmember

# 1. Number:
# number hocche je kono dhoroner songkha
# python a 3 type number royeche
"""
1. int
3. float
4. complex
"""

# int data type
# je kono dhoroner purno songkha ke int bole
safin = 520
print(type(safin))
print(safin)

#float data type
# doshomik jukto songkha ke float bole
mc = 20.5
print(type(mc))
print(mc)

#complex data type
# je data type a songkha er (j) thakle take comples data bole
bkcd = 2j
print(type(bkcd))
print(bkcd)

# 2. String
# je kono lekha ke "" or '' er moddhe lekha hole take string bole.
safin = 'mahfujur rahman safin'
print(type(safin))
print(safin)

firstName = 'Mahfujur Rahman'
lastName = 'Safin'
print("My name is " + firstName  + ' ' + lastName)
print(type(firstName + lastName))

#string formating methob
num1 = 5
num2 = 6
userName = "Safin"
roll = 10
print(f"this is my number is {num1 + num2}") # number string er vitor a dekhanor jonno
print(f"my name is {userName} & my roll is {roll}") # string er vitor string

# 3. boolean data type
# boolean data type holo ja sudhu matro duti value show korte pare 1. true or 2. false
a = True
b = False
print(type(a))
print(a )
print(b)

c = 8
d = 10
print( c >= d)

# 4. binary data type
# binary data type holo amon akti data type je khane (0) and (1) akare songrokkhon kora thake
"""
binary data type 3 dhoroner hoye thake
1. byte
2. bytearray
"""
# 1. byte
# byte holo immutable jeta akbar lekha hole seta ar change kora jay na, er range holo 0-255 porjonto
safinList = [2,8,7,10,23,55]
e = bytes(safinList)
print(type(e))

# 2. bytearray
# bytearry holo mutable jeta akbar lekha hole seta ar change kora jay, er range holo 0-255 porjonto
safinList1 = [2,8,7,10,23,55]
f = bytearray(safinList1)
f[1] = 100
print(f[1])

# 5. none data type
x = None
print(x)
print(type(x))

# 6. list
# square bracket er moddhe koma(,) er sahajje je value gula neoya hoy take list bole, list mutable
li = ['najim', 'sohan', 'sijol', 'mehek', 'jayed', 'toufik']
li[5] = 20
print(li)
print(type(li))

# 7. touple
# parentheses bracket er moddhe koma(,) er sahajje je value gula neoya hoy take touple bole, touple immutable
tup = ('najim', 'sohan', 'sijol', 'mehek', 'jayed', 'toufik', 20, 25, 85)
print(tup)
print(type(tup))

# 8. range
ran = range(10)
for i in ran:
    print(i)