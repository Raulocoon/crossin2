#抓取城市信息
#http://m.weather.com.cn/data3/city.xml
import urllib.request

url = "http://m.weather.com.cn/data3/city.xml"
url1 = "http://m.weather.com.cn/data3/city%s.xml"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
result = response.read().decode("UTF-8")
#00|省,01|北京,02|上海,03|天津,04|重庆,05|黑龙江,06
#print(result)

# 省份信息
provinces = result.split(",")
i = 0
result = "city = {\n"

try:

    for p in provinces:
        p_code = p.split("|")[0]
        p_name = p.split("|")[1]

        #调试数据
        if i > 0:
            #print("p_code : %s\tp_name : %s" %(p_code, p_name))
            urlCity = url1 % p_code
            #print(urlCity)

            requestCity = urllib.request.Request(urlCity)
            responseCity = urllib.request.urlopen(requestCity)
            resultcity = responseCity.read().decode("UTF-8")
            #print(resultcity)

            #城市信息
            #0501|哈尔滨,0502|齐齐哈尔,0503|牡丹江,0504|佳木斯,0505|绥化,0506|黑河,0507|大兴安岭,0508|伊春,0509|大庆,0510|七台河,0511|鸡西,0512|鹤岗,0513|双鸭山
            cities = resultcity.split(",")
            try:
                for c in cities:
                    c_code = c.split("|")[0]
                    c_name = c.split("|")[1]
                    #print("c_code : %s\tc_name : %s" % (c_code, c_name))
                    urlDistrict = url1 % c_code
                    #print(urlDistrict)

                    requestDistrict = urllib.request.Request(urlDistrict)
                    responseDistrict = urllib.request.urlopen(requestDistrict)
                    resultDistrict = responseDistrict.read().decode("UTF-8")
                    #print(resultDistrict)

                    #地区信息
                    #010101|北京,010102|海淀,010103|朝阳,010104|顺义,010105|怀柔,010106|通州,010107|昌平,010108|延庆,010109|丰台,010110|石景山,010111|大兴,010112|房山,010113|密云,010114|门头沟,010115|平谷,010116|八达岭,010117|佛爷顶,010118|汤河口,010119|密云上甸子,010120|斋堂,010121|霞云岭
                    districts = resultDistrict.split(",")


                    try:
                        for d in districts:
                            d_code = d.split("|")[0]
                            d_name = d.split("|")[1]
                            #print("d_code : %s\td_name : %s" % (d_code, d_name))
                            urlResult = url1 % d_code
                            #print(urlResult)

                            requestResult = urllib.request.Request(urlResult)
                            responseResult = urllib.request.urlopen(requestResult)
                            resultResult = responseResult.read().decode("UTF-8")
                            #print(resultResult)
                            name = d_name
                            code = resultResult.split("|")[1]
                            #print(name + "|" + code)
                            nameCode = "\t'%s':'%s',\n" %(name, code)

                            result += nameCode

                    except:
                        print("地区信息获取失败")

            except:
                print("城市获取失败")

            i+=1
            print(i)

        else:
            i+=1

except:
    print("省份获取失败")

#去掉最后一个逗号
result = result[:-2]
result += "\n}"

print(result)
f = open("city.py", "w")
f.write(result)
f.close()