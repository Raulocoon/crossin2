f = open("data.txt")
#dataRead = f.read()
#dataReadline = f.readline()
dataReadlines = f.readlines()

#print("dataRead ====>>>>>>>> " + dataRead)
#print("dataReadline ====>>>>>>>> " + dataReadline)
print("dataReadlines ====>>>>>>>> %r"  %(dataReadlines))

f.close()