'''
squID={
       "Ali":[130056, 128977],
       "Ahmed":130627,
       "Omar":135627
       }

for key in squID:
    if type(squID[key]) is list:
        count=1
        for i in squID[key]:
            print(key, i, count)
            count= count+1
    else:
        print(key, squID[key])
        
'''
'''
num=[2,1,5,3,3,1,5,1,10,9]
repsDic={}

for i in num:
    repsDic[i]= repsDic.get(i,0)
    repsDic[i] +=1
    
print(repsDic)



num=[2,1,5,3,3,1,5,1,10,9]
repsDic={}

for i in num:
    if i in repsDic:
        repsDic[i] +=1
        
    else:
        repsDic[i] =1
        
print(repsDic)


num=[2,1,5,3,3,1,5,1,10,9]
repsDic={}

for i in num:
    if i not in repsDic:
        repsDic[i] = num.count(i)
print(repsDic)

for key in repsDic:
    if repsDic[key]>1:
        print(key, "appered",  repsDic[key], "times" )

'''
'''

squID={
       "Ali":[130056, 128977],
       "Ahmed":130627,
       "Omar":135627
       }

for item in squID.items():
    print(item[0], item[1])
    if type(item[1]) is list:
        for i in item[1]:
            print(i)
 '''           
'''
squID={
       "Ali":[130056, 128977],
       "Ahmed":130627,
       "Omar":135627
       }

for value in squID.values():
    print(value)
    
for key in squID.keys():
    print(key)

'''
'''
t1=((1,2,3),("a","b","c"))

for i in t1:
    for j in i:
        print(j, end =" ")
    print()
    
    
t2=(1,2,3,1,5,1)
print(t2.count(1))
print(t2.index(1))

'''
'''
numberSet={1,2,3,4,3,2}
print(numberSet)

emptySet = set()
print(type(emptySet))

emptySet = {}  # this creat a dectionary
print(type(emptySet))

set_with_lists = set([1,2,3,4,5])  # convert from list to set
print(type(set_with_lists))
print(set_with_lists)

'''


records = [
    ("Ali", "Math", 85),
    ("Sara", "Math", 90),
    ("Ali", "Science", 78),
    ("Sara", "Science", 88),
    ("Ali", "English", 92),
    ("Sara", "English", 85)
]

newDec = {}

for record in range(len(records)):
    name = records[record][0]
    sub = records[record][1]
    grade = records[record][2]

    if name not in newDec:
        newDec[name] = {}
    
    newDec[name][sub] = grade

print(newDec)


subjects = {}

for name in newDec:
    for sub in newDec[name]:
        
        if sub not in subjects:
            subjects[sub] = []
        
        subjects[sub].append(newDec[name][sub])

for sub in subjects:
    total = 0
    
    for grade in subjects[sub]:
        total += grade
    
    avg = total / len(subjects[sub])
    print(sub, "average =", avg)




    
    
        
        
    
