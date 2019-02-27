first_name = input("What is your first name?  ")
print("Hello",first_name,"! ")
if first_name == "Cristian":
    print(first_name," is learning Python")
elif first_name == "Max":
    print(first_name," is learning with fellow students in the community!")
else:
    print("You should totally learn Python, {}".format(first_name))
print("Have a great day, {}\n".format(first_name))

