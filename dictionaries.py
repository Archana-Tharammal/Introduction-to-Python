"""mydict= {
    "brand": "Ford",
    "model": "mustang",
    "year":"1984"
}
thisdict=mydict.copy()
print(thisdict)

mydicts= {
    "brand": "Ford",
    "model": "mustang",
    "year":"1984"
}
thisdict=dict(mydicts)
print(thisdict)

myfamily={
    "child1":{
            "name":"emil" ,
            "year":"2004"
    },
    "child2":{
            "name":"tobias" ,
            "year":"2007"
    },
    "child3":{
            "name":"linus" ,
            "year":"2011"
    }

}
print(myfamily)

print(myfamily["child2"]["name"])

mydict= {
    "brand": "Ford",
    "model": "mustang",
    "year":"1984"
}

mydict.clear()
print(mydict)

mydict1= {
    "brand": "Ford",
    "model": "mustang",
    "year":"1984"
}
thisdict=mydict1.copy()
print(thisdict)

x=('key1','key2','key3')
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)

car= {
    "brand": "Ford",
    "model": "mustang",
    "year":"1984"
}
x=car.get("model")
y=car.items()
car["color"]="black"
print(x)
print(y)
print(car)

cars= {
    "brand": "Ford",
    "model": "mustang",
    "year":"1984"
}
z=cars.keys()
print(z)

car= {
    "brand": "Ford",
    "model": "mustang",
    "year":1984
}
car.pop("model")
print(car)
car.popitem()
print(car)"""

#create a dictionary
student={
    "first_name" :"Archana",
    "last_name" :"Tharammal",
    "gender" :"Female",
    "age" :22,
    "marital status" :"Single",
    "skills": "programming",
    "country" :"India",
    "city" :"Kannur",
    "address" :"Tharammal house, 7th mile"
}
print(student)
#length of the dictionary
print(len(student))

#get the value of skills
x = student.get("skills")
print(x)

# check the datatype and it should be list
y = list(student)
print(type(y))

#modify the skills values
student["skills"]="communication skills, problem solving skills"
print(student)

#get the keys as list
z = student.keys()
print(z)

#get the values as list
z = student.values()
print(z)

# change dict to a list of tuples using items() method
thisdict = student.items()
print(thisdict)

#delete one of the item
student.pop("age")
print(student)
