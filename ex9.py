#总游戏次数，最快猜出的轮数，和猜过的总轮数
from random import randint

#读取文件中的成绩数据
f = open("game.txt")
score = f.read().split()

#成绩分别保存在变量中
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

#计算平均时间
if game_times > 0:
    avg_times = float(total_times) / game_times
else :
    avg_times = 0

#输出起始成绩信息
print("你已经玩了[%d]次，最少[%d]轮猜出答案，平均[%.2f]轮猜出答案" %(game_times, min_times, total_times))

num = randint(1, 100)
print("Guess what I think?")
bingo = False
while bingo == False:
    answer = int(input())
    if answer < num:
        print("too small!")
    elif answer > num:
        print("too big!")
    else:
        print("BINGO!")
        bingo = True
