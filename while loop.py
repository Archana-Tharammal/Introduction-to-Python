#execute as long as condition is true
i=1
while i<11:
    print(i)
    i+= 1

#break statement
i=1
while i<5:
    print(i)
    if i==3:
        break
    i+=1

#continue statement
i=0
while i<11:
    i+=1
    if i==3:                 #3 is missing
        continue
    print(i)

#else statement
i=1
while i<8:
    print(i)
    i+=1
else:
    print("i is no longer less than 8")
