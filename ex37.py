# 字典也可以通过for...in遍历：
score = {
    '萧峰': 95,
    '段誉': 97,
    '虚竹': 89
}
print(score['虚竹'])

score['虚竹'] = 91
score['莫容复'] = 88
del score['萧峰']

for name in score:
    print(name + "\t" + str(score[name]))

