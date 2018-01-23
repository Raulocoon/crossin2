#f = open("data.txt", "a")
#f.write("You are not the last sentence, I am the one!\n")
#f.close()

#str = "just for the write test!!!\n"
#out = open("output.txt", "w")
#out.write(str)
#out.close()

#1.从一个文件中读出内容，保存至另一个文件。
readf = open("originalRead.txt")
data_read = readf.read()
writef = open("writeFromOriginal.txt","a")
data_write = writef.write(data_read)
readf.close()
writef.close()

#2.从控制台输入一些内容，保存至一个文件。
readStr = input(">>>> ")
f = open("strFromInput.txt", "w")
f.write(readStr)
f.close()
