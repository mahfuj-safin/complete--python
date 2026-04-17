"""
* variable er name akta word hote hobe
* variable er first er letter kono special case hote parbe nah
* pthon case sensitive, ekhane a and A er meaning different
* python er reserve keyword variable hisabe use kora jabe nah
* variable hisabe reserve keyword use kora best
* variable er name er pore (=) sing use kore value dile seita variable er value hisabe gonno hobe
* python a akta variable er man bar bar change kora jabe, etake bole re assign
* python a akoi line a ekadhik variable neoya jay
"""

print("Hello World")

firstName = "Safin" #firstName is variable, = is assignment, safin is value of variable
print(firstName)

a = b = c = 20 #python a akoi line a ekadhik variable neoya jay
print(a)


d, e, f = 15, 25, "Safin" #python a akoi line a ekadhik variable and sathe value neoya jay, se khetre variable gula k (,) dhara alada korte hobe
print(d)
print(e)
print(f)

#duti songkhar biyog fol nirnoy
val1 = int(input('enter first input: 10'))
val2 = int(input('enter second input: 20'))
result = val1 - val2
print(result)