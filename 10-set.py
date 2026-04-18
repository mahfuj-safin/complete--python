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