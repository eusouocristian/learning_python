import datetime
from peewee import *
from collections import OrderedDict
import sys
import os
from time import sleep

CharField()
# clean the terminal screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
clear_screen()

db = SqliteDatabase('diary.db')

class Entry(Model):
    #content
    content = TextField()
    #timestamp
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db

def initialize():
    """Create the database and the table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    """Show the Menu"""
    choice = None  #inicia a variavel sem valor atribuido

    #enquanto não se escolhe pra sair, permanece no loop
    while choice != 'q':   
        print('Type q to quit.')
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))  # value é uma função, então __doc__ é a docstring
        choice = input('Action: ').lower().strip() # strip retira espaços da string
        clear_screen()

        if choice in menu:
            menu[choice]()

def add_entry():
    """Add an Entry"""
    print('Enter your entry. Press ctrl + d when finished')
    # pega os valores digitados, inclusive multiplas linhas
    data = sys.stdin.read().strip()

    if data:
        if input('\nSave entry? [y/n]').lower() != 'n':
            Entry.create(content=data)
            clear_screen()

            print('Saved Successfully!')
            sleep(3)
            clear_screen()
        else:
            clear_screen()

def view_entries(search_query=None):
    """View previous Entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
        # entries = entries.where((variable1 == 'a') | (variable2 == 'b'))

    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(timestamp)
        print('='*len(timestamp))
        print(entry.content)
        print('\nn) Next Entry')
        print('d) Delete entry')
        print('q) return to main menu\n')

        next_action = input('Action: [N/d/q] ').lower().strip()

        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(entry)
            clear_screen()
            print('DELETED Successfully!')
            sleep(3)
            clear_screen()

def search_entries():
    """Search Entries for a string"""
    view_entries(input('Search Query: '))    


def delete_entry(entry):
    """Delete an Entry"""
    if input('Are you sure? [y/N').lower() == 'y':
        entry.delete_instance()


# cria um dict a partir de um tuple
menu = OrderedDict([
    ('a', add_entry), #key, value, sendo value uma função 
    ('v', view_entries), #idem
    ('s', search_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
