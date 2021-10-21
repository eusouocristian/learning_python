from dataclasses import dataclass
from typing import List
import shlex


def run_command(command: str) -> None:
    match command:
        case 'quit':
            print('Quitting the program')
            quit()
        case 'reset':
            print('Resetting the system')
        case other:
            print(f'Unknown command: {other!r}')


def run_command_v2(command: str) -> None:
    match command.split():
        case ['load', filename]:
            print(f'loading file: {filename}')
        case ['save', filename]:
            print(f'saving to file: {filename}')
        case ['exit' | 'quit' | 'bye']:        
            print('Quitting the program')
            quit()
        case _:
            print(f'Unknown command: {command!r}')


def run_command_v3(command: str) -> None:
    match command.split():
        case ['load', filename]:
            print(f'loading file: {filename}')
        case ['save', filename]:
            print(f'saving to file: {filename}')
        case ['exit' | 'quit' | 'bye', *rest] if '--force' or '-f' in rest:
            print('Sending SINGTERM to all processes and quitting the program.')
            quit()
        case ['exit' | 'quit' | 'bye']: 
            print('Quitting the program')
            quit()
        case _:
            print(f'Unknown command: {command!r}')



@dataclass
class Command:
    """Class thar represents a command."""

    command: str
    arguments: List[str]

def run_command_v4(command: Command):
    match command:
        case Command(command="load", arguments=[filename]):
            print(f'loading file: {filename}')
        case Command(command="save", arguments=[filename]):
            print(f'saving to file: {filename}')
        case Command(command='exit' | 'quit' | 'bye', arguments=['--force' | '-f', *rest]):
            print('Sending SINGTERM to all processes and quitting the program.')
            quit()
        case ['exit' | 'quit' | 'bye']: 
            print('Quitting the program')
            quit()
        case _:
            print(f'Unknown command: {command!r}')
 



def main():
    """ Main Function """

    while True:
        # command = input("$ ")
        # run_command_v3(command)

        command, *arguments = shlex.split(input('$ '))
        run_command_v4(Command(command, arguments))


if __name__ == "__main__":
    main()