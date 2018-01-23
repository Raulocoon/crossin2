import pickle

test_data = ['Save me!', 123.456, True]
f = open('test.data', 'wb')
pickle.dump(test_data, f)
f.close()

f2 = open('test.data', 'rb')
antiTxt = pickle.load(f2)
f2.close()
print(antiTxt)
print(type(antiTxt))
