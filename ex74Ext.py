import urllib.request
import time
import threading

data = []
start_time = time.time()

def write_file(data):
    with open("douban_movie_ext.txt", "w") as f:
        f.writelines(str(data) + "\n")

def get_douban_movie(i):
    id = 1764796 + i
    print(id)
    url = "https://api.douban.com/v2/movie/subject/%d" % id
    try:
        req = urllib.request.Request(url)
        res = urllib.request.urlopen(req)
        con = res.read().decode("UTF-8")
        data.append(con)
        #data.append(con)
        print(i, time.time() - start_time)
        print('data:', len(data))
        write_file(data)
    except:
        print("exception")

for i in range(20):
    print("Requesting movie from douban...... ", i)
    threading.Thread(get_douban_movie(i))