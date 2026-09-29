
dic = {1: 'python' , 2: 'java' , 3: 'C programming'  }

##dic.clear()
dic1 = dic.copy()

print(dic.get(4, 'Key is not exist'))
##print(dic[4])

print(dic.items())
print(dic.keys())
dic.pop(2)
dic.popitem()
dic.update({4 : 'Go' , 5 :'R'})
print(dic.values())
