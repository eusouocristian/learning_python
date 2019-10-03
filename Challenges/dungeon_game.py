import random

# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for the monster
# draw player in the grid
# take input for movement
# move player, unless invalid move (past edges of grid)
# Check for Win/Loss
# Clear the screen / redraw the grid

# each cell = (x,y)
CELLS = [(0,0), (1,0), (2,0), (3,0), (4,0), 
         (0,1), (1,1), (2,1), (3,1), (4,1),    
         (0,2), (1,2), (2,2), (3,2), (4,2),
         (0,3), (1,3), (2,3), (3,3), (4,3),
         (0,4), (1,4), (2,4), (3,4), (4,4)]

def get_locations():
    door = None
    monster = None
    player = None
    return door, monster, player

def move_player(player, move):
    # get the players location
    # if move == LEFT, x-1
    # if move == RIGHT, x+1
    # if move == UP, y+1
    # if move == DOWN, y-1
    return player

def get_moves(player):
    moves = ["UP", "DOWN", "RIGHT", "LEFT"]
    # if player's y == 0, they can't move up
    # if player's y == 4, they can't move down
    # if player's x == 0, they can't move left
    # if player's x == 4, they can't move right
    return moves
    







while True:
    print("Welcome to the Dangeon!")
    print("You are currently in the room {}") # Fill with player position
    print("You can move {}") # Fill with available moves
    print("Enter QUIT to quit")

    move = input("> ").upper()
    
    if move == 'QUIT':
        break

    # Good Move? Change the player position
    # Bad Move? Don't change Anything
    # On the door? They Win!
    # On the monster? They Lose!
    # Otherwise, loop back around
