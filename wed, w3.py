dic = {
    "Sunday": 30,
    "Monday": 29,
    "Tuesday": 31,
    "Wednesday": 33,
    "Thursday": 35,
    "Friday": 28,
    "saturday": 25   
    }
'''
print(len(dic))

print(dic["Wednesday"])

for key in dic:
    print(key, dic[key])
'''
'''
# from dictionary to list[] of tuiple()......[(,),(,),(,)]

lastWeekTemp =[]
for key in dic:
    lastWeekTemp.append((key, dic[key]))
    
'''
'''
# find the average for dictionary
totalTemp=0
for key in dic:
    totalTemp = totalTemp +dic[key]
    
avgTemp= totalTemp / len(dic)


# another way for sum, use sum function  
print(sum(dic.values()))

# max and min
print(max(dic.values()))
print(min(dic.values()))



# find max and min , using loop 
maxm = 0
for value in dic.values():
    if value > maxm:
        maxm = value

minm = 100
for value in dic.values():
    if value < minm:
        minm = value
'''        
'''
# (.items) used for ----> dic to tiuple

maxm = 0
for value in dic.values():
    if value > maxm:
        maxm = value
        
for item in dic.items():
    print(item[0], item[1])
    if item[1] == maxm:
        print("This max temp was on day: ", item[0])
        
'''
'''
maxm = 0
for value in dic.values():
    if value > maxm:
        maxm = value
        
for day, temp in dic.items():
    if temp == maxm:
        print(day)
'''


