"""#creating a function
def my_function():
    print("hello world")

my_function()

#arguements
def my_func(fname):
    print(fname+ " "+"Refsnes")
my_func("Emil")
my_func("Tobias")
my_func("Linus")

#function with two arguements
def my_function(fname, lname):
    print(fname +" "+ lname)
my_function("Emily","Joseph")

#arbitrary arguements
def my_functions(*kids):
    print("The youngest child is " +kids[2])
my_functions("Emil","Tobias","Linus")

def my_function(child3,child2,child1):
    print("The youngest child is "+ child3)
my_function(child1="Emil", child2="Tobias", child3="Linus")

def my_func(**kid):
    print("his last name is "+ kid["lname"])
my_func(fname="Tomy", lname="Refnes")"""

#default parameter value
def my_func(country="Norway"):
    print("I'm from " +country)
my_func()
my_func("Sweden")
my_func("India")

#passing a list as an arguement
def my_func(food):
    for x in food:
        print(x)
fruits=["Apple","Orange","Banana"]
my_func(fruits)
