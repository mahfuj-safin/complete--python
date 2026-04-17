# list

li = [ 1, 2, 3, 4, 5 ]
print(li)
li[2] = 100
print(li)

lis = [ "safin", "mahfuj", "mishe", "safat", "rahat"]
print(lis)
lis[3] = 10
print(lis)

list = [True, False, True, False]
print(list)

#Access Items
safin = ["channleName", "page", "webSite", "group", "asd;jafhasdkj"]
print(safin)
print(safin[1])

#Change Item Value
safin[4] = "facebook page"
print(safin)

#Add List Items
# list item add kora jay duita upay append() method and insert() method
# append
safin.append(10) # append diya kono kisu add kora hole seta add hoy sobar last
print(safin)

#Insert Items
safin.insert(1, "google page") # insert korar maddhome je index number use kora hobe tar age add hobe
print(safin)


#Remove List Items

# the remove() method
safin1 = ["channleName", "page", "webSite", "group", "asd;jafhasdkj"]
safin1.remove("webSite") # remove korte hole specific name call korte hobe
print(safin1)

#The pop() method removes the specified index.
safin2 = ["channleName", "page", "webSite", "group", 420]
safin2.pop(4)
print(safin2)

#If you do not specify the index, the pop() method removes the last item.
safin3 = ["channleName", "page", "webSite", "group", 850, 850]
safin3.pop()
print(safin3)


#The del keyword also removes the specified index:
safin4 = ["channleName", "page", "webSite", "group", 850, 850]
del safin4[0]
print(safin4)

#The clear() method empties the list.
safin4.clear()
print(safin4)


#Python - Loop Lists

#You can loop through the list items by using a for loop:
loopList = ["raisa", "ayeda", "maliha", "eva", "sathi"]
for prem in loopList:
    print(prem)


#Use the range() and len() functions to create a suitable iterable.

for i in range(len(loopList)):
    print(i)


#Print all items, using a while loop to go through all the index numbers
y = 0
while y < len(loopList):
    print(loopList[y])
    y += 1


#List Comprehension
safinList = [1,2,4,5]
double = [i ** 2 for i in safinList]
print(double)


#Sort Lists

#ascending
number = [5,4,8,7,1,3,14,85,15,95,16]
eng = ["g","s","k","a","k","b","o"]
number.sort()
eng.sort()
print(eng)
print(number)

#Descending
num = [1,2,3,4,5,6,7,8,9]
num.sort(reverse = True)
print(num)

#Python - Copy Lists
number1 = [1,2,3,4,5,6,7,8,9]
print(number1)
sanum = number1.copy()
print (sanum)

#Python - Join Lists
list1 = ["A","B","C",]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)