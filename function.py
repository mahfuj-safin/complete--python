#requierd argument
def add(a,b,c):
    d = a+b+c
    return d
print(add(1,2,3))

#keyword argument
def student(name, roll):
    print(name)
    print(roll+5)
    return name,roll
student(roll=2, name="Safin")

#default argument
def add(a,b,c=5):
    d = a+b+c
    return d
print(add(2,20))

#variable lenth argument
def add(a,*b):
    print(a)
    print(b)
    c=a
    for i in b: #function theke value gula ber korar jonno
        c=c+i
    print(c)
add(2,5,8,9,5)

#today date janar jonno date.today() use korte hobe
from datetime import date
today = date.today()
print(today)

#yesterday date ber korar program
from datetime import date, timedelta
def yesterday():
    today = date.today()
    print("today's date is", today)
    yesterday = today - timedelta(days=1)
    print("yesterday date is", yesterday)
    return today, yesterday
yesterday()

#agami diner tarikh janar jonno
from datetime import date, timedelta
def tomorrow():
    today = date.today()
    print("today's date is", today)
    tomorrow = today + timedelta(days=1)
    print("tomorrow date is", tomorrow)
    return today, tomorrow
tomorrow()


#date and time and combine
from datetime import datetime, date
def combine():
    # current time
    t = datetime.now().time()
    print('time is', t)
    # current date
    d = date.today()
    print('today is', d)
    # combine
    dt = datetime.combine(d, t)
    print('today time and date', dt)
    return t, d, dt
combine()

#duti songkhar moddhe boro songkha
def largest():
    num1 = 20
    num2 = 19
    if num1 > num2:
        print("the largest number is", num1)
    else :
        print("the smallest number is", num2)
    return num1, num2
largest()
