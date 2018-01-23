import urllib.request
from city import city
import json

exit = False

while not exit:
    cityName = input("请输入你要查询的城市（输入q\Q退出） >>> ")

    if cityName == "q" or cityName == "Q":
        print("已退出！")
        exit = True
    else:
        cityCode = city.get(cityName)

        if cityCode:
            try:
                url = ("http://www.weather.com.cn/data/cityinfo/%s.html" %cityCode)
                request = urllib.request.Request(url)
                response = urllib.request.urlopen(request)
                content = response.read().decode("utf-8")
                #print(content)

                data = json.loads(content)
                dataContent = data['weatherinfo']
                dataResult = ("%s : %s\t%s ~ %s") %(cityName, dataContent['weather'], dataContent['temp1'], dataContent['temp2'])
                print(dataResult)
            except:
                print("查询失败")

        else:
            print("没有找到该城市。")