
#Student Marks Manager


marks = []
n = int(input("how many subject?"))
for b in range(n):
    m = float(input("Enter marks:"))
    marks.append(m)
total = sum(marks)
avg = total / n
print(marks)
print(total)
print(avg)


#To-Do List App

tasks = []

while True:
    print("\n1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
        else:
            print("Task not found")

    elif choice == "3":
        print("Tasks:", tasks)

    elif choice == "4":
        break



#Shopping Cart System


cart = []
while True:
    item = input("Enter item price(or q to quit): ")
    if item == "q":
        break
    cart.append(float(item))
total = sum(cart)
print("cart item:", cart)
print("total bill:", total)

# topper finder
student = ['safin', 'eva', 'maisa']
marks = [85,81,83]
top_mark = max(marks)
index = marks.index(top_mark)
print("topper:", student[index])
print("marks:", top_mark)

#Duplicate Remover
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print("Unique list:", unique)

