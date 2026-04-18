#set
# set is unchangeable
# set kerlibasis er moddhe likhte hoy
# set is unorder
# set duplicate kora jay na
# set a len() function support kore


mySet = {1, False, "Safin",5,6,9}
print(mySet)
print(type(mySet))
print(len(mySet))


#Access Set Items
#for loop er maddhome
for i in mySet:
    print(i)

print(10 in mySet)


#Add Set Items

mySet1 = {"safin", "tutul", "shakil", "najim"}
mySet1.add("sohan")
print(mySet1)

#set update method
mySet2 = {"safin", "tutul", "shakil", "najim"}
set3 = {1,2,3}
mySet2.update(set3)
print(mySet2)


#Remove Set Items
Myset = {1,2,3,4,5,6}
Myset.remove(5)
print(Myset)

#discard() method: # value na thakleo error dibe na
MySet = {1,2,3,4,5,6}
MySet.discard(12)
print(MySet)

#pop() method:
MySet1 = {"safin", "mehek", "toufik"}
MySet1.pop()
print(MySet1)

#clear() method
MySet2 = {"safin", "mehek", "toufik"}
MySet2.clear()
print(MySet2)


#Loop Sets
MySet3 = {"safin", "mehek", "toufik"}
for i in MySet3:
    print(i)

#Join Sets
#union() method
MySet4 = {"safin", "mehek", "toufik"}
MySet5 = {1,2,3,4,5,6}
set = MySet4.union(MySet5)
print(set)

#update method
MySet5 = {"safin", "mehek", "toufik"}
MySet6 = {1,2,3,}
MySet6.update(MySet5)
print(MySet6)