f = open("score.txt")
lines = f.readlines()  #取得文件中的数据。因为每一行都是一条学生成绩的记录，所以用readlines，把每一行分开，便于之后的数据处理
#print(lines)
f.close()

#保存个人总成绩
results = []

for line in lines:
    #print(line)
    data = line.split()
    #print(data)

    sum = 0
    for score in data[1:]:
        point = int(score)
        if point < 60:
            continue
        sum += int(score)

    result = "%s \t : %d\n" %(data[0], sum)   #姓名，个人总成绩
    #print(result)

    results.append(result)
    #print(results)

#print(results)
output = open("result.txt", "w")
output.writelines(results)
output.close()
