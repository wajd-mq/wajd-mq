
dic = {
    "Sunday": [30,29],
    "Monday": [29,31],
    "Tuesday": [31,30],
    "Wednesday": [33,32],
    "Thursday": [35,33],
    "Friday": [28,30],
    "saturday": [25,23],
    
    }

'''
for day, temps in dic.items():
    print(day, temps)


# print week 1 temps only:    
for day, temps in dic.items():    
    print(day, temps[0])
    
'''
'''
totalTemp=0
for key in dic:
    totalTemp = totalTemp +dic[key][1]
    
avgTemp= totalTemp / len(dic)
print(avgTemp)

#################

totalTemp=0
for day, temps in dic.items():
    totalTemp+= temps[1]
avgTemp= totalTemp / len(dic)
print(avgTemp)
'''
'''
#appending by enter input
for day in dic:
    newTemp=int(input("Enter new temp: "))
    dic[day].append(newTemp)

print(dic)

'''
'''
for key in dic.keys():
    newTemp=int(input("Enter new temp for "+ key+ " for week3: "))
    dic[key].append(newTemp)

print(dic)
'''


# appending list
lis=[30,28,28,32,26,35,36]

index =0
for key in dic.keys():
    dic[key].append(lis[index])
    index +=1
    
print(dic)

    
