import logging

#criar arquivo de log com nome 'logging.log' na pasta onde esta rodando o codigo .py
logging.basicConfig(filename='loggin.log', level=logging.DEBUG)
loggin.info('informacoes iniciais')
# Levels:
# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG
# NOTSET (never used)

# é possivel gravar dados no arquivos de log,
# logging.debug('Valor da variavel: {}'.format(variavel_value))
# logging.warning('Texto aqui')
# ----------------------------
# python debugger:
import pdb; pdb.set_trace()
# a partir desse ponto, o codigo ira executar linha por linha
# pode-se verificar o valor das variaveis apos cada execucao de linha
# pressiona-se 'n' para proxima linha e 'q' pra sair, 'c' para continuar sem parar nas linhas seguintes
# pesquisar outros comandos


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


