# from turtle import Turtle, Screen
#
# bob = Turtle()
# print(bob)
# bob.shape("turtle")
# bob.color("red")
# bob.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Charizard", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)