from graphics import *

win = GraphWin('LifeDecisions', 400, 400)

start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

user_input = input("Type 'left' to go left or 'right' to go right.")
if user_input.lower() == "left":
    print("You decide to go left and a very hungry monkey eats you alive")

elif user_input.lower() == "right":
    print("You choose to go right and a very big giraffe eats you alive")

else:
    print("You fail to give clear instructions so a giant whale eats you alive!")
