from random import randint

#输入玩家名字
name = input("请输入你的名字：")

f = open("game.txt")
lines = f.readlines()
f.close()

# 初始化一个空字典
scores = {}
for l in lines:
    s = l.split()  #按行拆分
    scores[s[0]] = s[1:]

# 查找当前玩家的数据
score = scores.get(name)

# 初始化玩家数据
if score is None:
    score = [0, 0, 0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])

# 平均成绩
if game_times > 0:
    avg_times = float(total_times) / game_times
else:
    avg_times = 0

# 显示初始信息
print("[%s], 你已经玩了[%d]次，最少[%d]轮猜出答案，平均[%.2f]轮猜出答案" %(name, game_times, min_times, total_times))

# 开始
num = randint(1, 100)
times = 0
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

#将成绩更新到对应的玩家数据中
scores[name] = [str(game_times), str(min_times), str(total_times)]
#玩家数据存储
result = ''
for n in scores:
    #成绩格式化，结尾换行
    line = n + " " + " ".join(scores[n]) + "\n"
    result += line

f = open("game.txt", "w")
f.write(result)
f.close()

