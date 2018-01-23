#-*- coding: cp936 -*-
#https://api.douban.com/v2/movie/subject/1764796
#抓取豆瓣电影评论

import urllib.request
import time

start_time = time.time()
data = []
for i in range(10):
    print("Requesting movie from douban...... ", i)
    id = 1764796 + i
    print(id)
    url = "https://api.douban.com/v2/movie/subject/%d" %id

    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        con = res.read().decode("UTF-8")
        data.append(con)
        print(i, time.time() - start_time)
    except:
        continue

print('data:', len(data))
f = open("douban_movie.txt", "a")
f.write(str(data))
f.close()