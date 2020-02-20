# multiple imports
def fooBar(arg1,arg2,arg3,arg4):
         # way too much indentation
         return arg1,arg2,arg3,arg4
def bar(*args):
    # bad spacing
    return 2+2

# Bad class name, bad spacing, bad indentation
class treehouse:
   def one(self):
      return 1
   def two(self):
      return 2

import sys, random


# bad identation and whitespace
a,b,c,d=fooBar ( "a long string","a longer string","yet another long string",
  "and other crazy string"
    )


# bad spacing
one      = 1
three    = 3
fourteen = 14 # make fourteen equal to 12

print( a )
print(fourteen)

print(treehouse().two())

import pep8
checker = pep8.Checker('badpep8.py')
checker.check_all()