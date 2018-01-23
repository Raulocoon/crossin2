from random import randint

# 读取起始成绩
f = open("game.txt")
score = f.read().split()
f.close()

#分别定义成绩列
game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

#平均成绩
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0

# 输出起始成绩
print("你已经玩了[%d]次，最少[%d]轮猜出答案，平均[%.2f]轮猜出答案" %(game_times, min_times, total_times))

# 随机数
num = randint(1, 100)
times = 0 #记录本轮次数
print("Guess what I think?")
bingo = False

while bingo == False:
    times += 1
    answer = int(input())

    if answer < num:
        print("too small!!!")
    elif answer > num:
        print("too big!!!")
    else:
        print("BINGO!!!")
        bingo = True

#如果是第一次玩，或者本轮轮数比最小轮数小，则更新最小轮数
if game_times == 0 or times < min_times:
    min_times = times

total_times += times    #总游戏次数增加
game_times += 1 #游戏次数加1
result = "%d %d %d" %(game_times, min_times, total_times)
f = open("game.txt", 'w')
f.write(result)
f.close()




