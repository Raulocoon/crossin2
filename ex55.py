import re

text = "Hi, I am Shirley Hilton. I am his wife."

res = re.findall(r"[Hi]", text)

if res:
    print(res)
else:
    print("Not found!")

#Greedy match
res2 = re.findall("l.*e", text)
if res2:
    print(res2)
else:
    print("Not found2!")

#lazy match
res3 = re.findall("l.*?e", text)
if res3:
    print(res3)
else:
    print("Not found3!")

#lazy match
res4 = re.findall("l.*e?", text)
if res4:
    print(res4)
else:
    print("Not found4!")

# start with "s", end with "e"
text2 = "site sea sue sweet see case sse ssee loses"
res5 = re.findall("s.*?e", text2)
if res5:
    print(res5)
else:
    print("Not found5!")

# \b start or end
res6 = re.findall(r"\bs\S*e\b", text2)
if res6:
    print(res6)
else:
    print("Not found6!")