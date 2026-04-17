#  touple

newTouple = ('safin', 'mahfuj', 'najim', 'rahat', 1,2,3, 20)
print(type(newTouple))

#Access Tuple Items

#You can access tuple items by referring to the index number, inside square brackets
# newTouple[5] = 8 immutable
print(newTouple[6])
# negetive indexing
print(newTouple[-1])

#Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#Change Tuple Values

list1 = ('sfin', 'mahfuj', 'najim', 'rahta',20,30)
a = list(list1)
a.append("eva")
b = tuple(a)
print(b)
print(type(b))

# Unpack Tuples
fruits = ("apple", "banana", "cherry")
(a,b,c )= fruits
print(b)

#Using Asterisk*
fruits1 = ("apple", "banana", "cherry", "egg", "mango", "vanala", "chocolate")
(a,b,*c, d) = fruits1
print(c)


#Loop Tuples
lis = ("raisa", "eva", "mishe", "ayeda", "maliha")
for x in lis:
    print(x)
for y in range(len(lis)):
    print(lis[y])

crush = ("raisa", "eva", "mishe", "ayeda", "maliha")
i = 0
while i < len(crush):
    print(crush[i])
    i += 1


# Join Tuples
num1 = (1, 2, 4)
num2 = (5, 6, 7)
num3 = num1 + num2
print(num3)


#Multiply Tuples
num4 = (5, 6, 7)
num5 = num4 * 2
print(num5)

# count() method
saf = (5,5,5,5,8,4,7,9, 6,8,4,8,9,4,6,5,7,8)
safi = saf.count(4)
print(safi)

#index()
name = ("safin", "mahfuj", "najim", "rahat")
name1 = name.index("najim")
print(name1)