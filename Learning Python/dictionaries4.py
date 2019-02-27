# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.

def num_teachers(arg):
    number_of_teachers = len(arg.keys())
    return number_of_teachers

def num_courses(arg):
    value = 0
    for key in arg.keys():
        value += len(arg[key]) 
    return value

def courses(arg):
    course = []
    for key in arg.keys():
        value = 0
        while(value < len(arg[key])):
            course.append(arg[key][value])
            value += 1
    return course

def most_courses(arg):
    value = 0
    for key in arg.keys():
        if len(arg[key]) > value:
            value = len(arg[key])
            professor = key
        else:
            continue
    return professor   

def stats(arg):
    stats_list = []
    for key in arg.keys():
        value = len(arg[key])
        stats_list.append([key,value])
    return stats_list  



# The dictionary will look something like:
arg = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
'Kenneth Love': ['Python Basics', 'Python Collections'],
'Cristian Santos': ['Matlab', 'Control','Linear Systems','MPC']}
print(num_courses(arg))
print(courses(arg))
print(most_courses(arg))
print(stats(arg))



