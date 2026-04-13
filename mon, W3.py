'''
listt = [1, 2, 2, 5, 4, 5, 3, 5, 4]
newlist=[]
for i in range(len(listt)):
    rep=1
    for j in range(i+1, len(listt)):
        if listt[i] in newlist:
            break
        if listt[i] == listt[j]:
            rep+=1
            
    if rep>1:
        newlist.append(listt[i])
        print(listt[i], rep)
'''
'''
lis = [1, 2, 2, 5, 4, 5, 3, 5, 4]
checked=[]

for i in lis:
    rep=0
    if i not in checked:
        for j in lis:
            if i==j:
                rep=rep+1
        checked.append(i)
        if rep>1:
            print(i, "reptead", rep, "times")
            
'''
'''
friend= ["Ali", "Mohammed", "jawhara", "mona"]

friend.insert(1,'wajd')

print(friend)
'''
'''
friend= ["Ali", "Mohammed", "jawhara", "mona"]
x=1
friend.append(" ")
for i in range(len(friend), x,-1):
    friend[i] = friend[i-1]
    
friend[x]="Wajd"
print(friend)
'''


friend= ["Ali", "Mohammed", "jawhara", "mona"]
'''
# insert
friend.insert(1,'wajd')
print(friend)

#finding
if "wajd" in friend:
    print("she is a friend")
    
#finding an element
n=friend.index("mona")
print(n)

#removing
friend.pop(1)
friend.remove("Ali")
print (friend)


#concatenation
list2=["meem", "noor"]
newList= friend+list2
print(newList)

#replication
newList= friend *2
print(newList)
'''
'''
def multiply(lis, factor):
    lis=list(lis) # thire we make a copy for the list , so will be no change in the origin list 
    for i in range(len(lis)):
        lis[i]= lis[i] * factor
    return lis

listt=[2,4,6]
factor=2
print(multiply(listt, factor))
print(listt)
'''
'''
temp= [12,34,56,78,90,77,65,54,34,23,22,11]
thirdQuerter=temp[6:9]
print(thirdQuerter)

fourthQuerter=temp[9:12]
print(fourthQuerter)

fourthQuerter1=temp[9:]
print(fourthQuerter1)

firstQuerter=temp[0:3]
print(firstQuerter)

firstQuerter1=temp[:3]
print(firstQuerter1)

allList=temp[:]
print(allList)

#update some values
temp[0:3]=[1, 1, 1]
print(temp)
'''
'''
values=[2, 100, 30, 40]
limet=99
pos=0
found = False
while pos< len(values) and not found:
    if values[pos]>limet:
        found = True
    else:
        pos= pos+1

if found:
    print("pos: ", pos)

else:
    print("not found")
'''
'''
medal=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

for i in range (len(medal)):
    
    for j in range(len(medal[i])):
        print(medal[i][j], end=" ")
    print()
'''

''' 

matrix=[
    [2,4,5,1],
    [3,2,9,6],
    [1,0,2,10]
    ]
totals=[]    
for row in range(len(matrix)):
    total=0
    for j in range(len(matrix[row])):
        total = total+ matrix[row][j]
    totals.append(total)
maxx= max(totals)
print(totals.index(maxx))

'''
'''
matrix=[
    [2,4,5,1],
    [3,2,9,6],
    [1,0,2,10]
    ]

for row in range(len(matrix)):
    print(matrix[row][0])
'''
'''
matrix=[
    [2,4,5,1],
    [3,2,9,6],
    [1,0,2,10]
    ]

print(matrix[0:2])
 '''
'''
matrix=[
    [2,4,5,1],
    [3,2,9,6],
    [1,0,2,10]
    ]
for row in range(2):
    print(matrix[row][-1])
 '''
'''
matrix=[
    [2,4,5,1],
    [3,2,9,6],
    [1,0,2,10]
    ]
for row in range(len(matrix)):
    print(matrix[row][0],matrix[row][1] )
 '''


squID={
       "Ali":"130056",
       "Ahmed":"130627",
       "Omar":"135627"
       }

aliID= squID["Ali"]
print(aliID)

ahmedID= squID["Ahmed"][0]
print(ahmedID)

if "Ali" in squID:
    aliID= squID["Ali"]
    print(aliID)
    
# defult    
print(squID.get("Ahmed", 411))
print(squID.get("Reem", "not found"))

# for change 
squID["Omar"]=233345
print(squID)
    
