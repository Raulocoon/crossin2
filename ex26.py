# 【Python 第26课】 操作list
#==== 点球小游戏 ====#
from random import choice
print("Choose one side to shoot:")
print("left, center, right")
you = input()
print("You kicked " + you)

direction = ["left","center","right"]
com = choice(direction)
print("Computer saved " + com)

if you != com :
   print("Goal!")
else :
   print("Oops...")
