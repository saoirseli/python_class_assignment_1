n = input("What is your name?\n")

name= n.split(" ")
firstname = name[0].lower()
lastname = name[1].lower()
newfirstname = firstname.capitalize()
newlastname = lastname.capitalize()

h = "Hello,"

print(h, newfirstname, newlastname)

