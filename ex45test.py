#写入byte格式的内容，要用wb模式打开文件才行，w模式打开的文件不能正常写入
#http://qq.ip138.com/weather/shanxi/taiyuan.htm  可查  但是好像没有山西省的天气。。。
#北京地区。。。不能查全北京的天气，只能查具体的某个区，比如北京昌平

import urllib.request
url1 = 'http://qq.ip138.com/weather/'
province = input('用拼音输入省份\n')
city = input('用拼音输入城市\n')
url = url1+province+'/'+city+'.htm'
request = urllib.request.Request(url)
content = urllib.request.urlopen(request)
print(content.read().decode("UTF-8"))
