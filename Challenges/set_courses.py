# Let's write some functions to explore set math a bit more. We're going to be using 
# this COURSES dict in all of the examples. Don't change it, though!
# So, first, write a function named covers that accepts a single parameter, a set of topics. 
# Have the function return a list of courses from COURSES where the supplied set and the course's 
# value (also a set) overlap.
# For example, covers({"Python"}) would return ["Python Basics"].

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


set_out = set([])
def covers(set_topics1):
    if set_topics1 & COURSES["Python Basics"]:
        set_out.add("Python Basics")
    if set_topics1 & COURSES["Java Basics"]:
        set_out.add("Java Basics")
    if set_topics1 & COURSES["PHP Basics"]:
        set_out.add("PHP Basics")
    if set_topics1 & COURSES["Ruby Basics"]:
        set_out.add("Ruby Basics")
    return set_out

a = covers(set(["Python"]))
print(a)

# Great work!
# OK, let's create something a bit more refined. Create a new function named covers_all 
# that takes a single set as an argument. Return the names of all of the courses, in a list, 
# where all of the topics in the supplied set are covered.
# For example, covers_all({"conditions", "input"}) would return ["Python Basics", "Ruby Basics"]. 
# Java Basics and PHP Basics would be excluded because they don't include both of those topics.

set_out2 = [] 
def covers_all(set_topics):
    if set_topics & COURSES["Python Basics"] == set_topics:
        set_out2.append("Python Basics")
    if set_topics & COURSES["Java Basics"] == set_topics:
        set_out2.append("Java Basics")
    if set_topics & COURSES["PHP Basics"] == set_topics:
        set_out2.append("PHP Basics")
    if set_topics & COURSES["Ruby Basics"] == set_topics:
        set_out2.append("Ruby Basics")
    return set_out2

b = covers_all({"conditions", "input"})
print(b)