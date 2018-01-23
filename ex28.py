from random import choice

score = [0, 0]
direction = ["left", "center", "right"]

def kick():
    print("++++ You kick! ++++")
    print("Choose one side to shoot!")
    print("left, center, right")
    you = input()
    print("You kickd " + you)
    com = choice(direction)
    print("Computer kicked " + com)

    if you != com:
        print("Goal!")
        score[0] += 1
    else:
        print("Ooops ...")

    print("Score Kicked: %d(you) - %d(com)" %(score[0], score[1]))

    print("==== You Save! ====")
    print("Choose one side to save!")
    print("left, center, right")
    you = input()
    print("You saved " + you)
    com = choice(direction)
    print("Computer saveed " + com)

    if you == com:
        print("Saved!")
    else:
        print("Ooops...")
        score[1] += 1

    print("Score Saved: %d(you) - %d(com)" % (score[0], score[1]))

for i in range(5):
    print("for **** Round %d" %(i+1))
    kick()

while():
    i += 1
    print("while **** Round %d" % (i + 1))
    kick()

if score[0] > score[1]:
    print("You win!")
else:
    print("You Lose!")
