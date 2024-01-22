fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)

for x in "cherry":
    print(x)

#break statement
fruits=["apple","banana","cherry","orange"]
for x in fruits:
    print(x)
    if x=="cherry":
        break

#continue statement
fruits=["apple","banana","cherry","orange"]
for x in fruits:
    if x=="banana":
        continue
    print(x)

#range function
for x in range(11):
    print(x)

for x in range(0,50,10):
    print(x)

#else in loop
for x in range(6):
    print(x)
else:
    print("finally finished!")

#nested loops
adj=["red","big","tasty"]
fruits=["apple","banana","cherry","orange"]
for x in adj:
    for y in fruits:
        print(x,y)

#pass statement
for x in range(2,100,5):
    pass
