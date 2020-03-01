# multiple imports
def fooBar(arg1,arg2,arg3,arg4):
   '''Esse é um codigo de exemplo para mostrar
   como se faz a documentacao de uma funcao ou classe.
   Pode-se portanto, utilizar nesse caso a função 'help(badpep8.fooBar)'
   para verificar o que ela faz'''
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


# thats possible to install pep8 or flake8
# pep8 changed for 'pycodestyle'
# python -m pip install pycodestyle
# https://pypi.org/project/pep8/0.4/#files
# https://flake8.pycqa.org/en/latest/
# https://legacy.python.org/dev/peps/pep-0008/

# EASTER EGG ON PYTHON
## just type 'import this' on the python shell


