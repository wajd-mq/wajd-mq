'''
values = ["","Mohammed", 66,55, "Ali"]

print(len(values))

print(values[3])

name= values[4]
print (name[0])

print(values[4][1]) #sequance inside sequence

print(values[1][len(values[1])-1]) #last letter

print(values[1][len(values[1])//2 ]) #midel latter


value =[]
value.append(20)
value.append(30)
value.append(40)
print(value)


value1 =[1,2]
value1.append(20)
value1.append(30)
value1[1] = 5
print(value1)
'''
'''
grades=[]

for i in range(5):
    grade =float(input("Enter a grade: "))
    grades.append(grade)
print(grades)


for grade in range(len(grades)):
    print(grades[grade])
    
    
for grade in grades:
    print(grade)
    
'''
'''
values=[5, 9, 11, 17, 4]
x =int(input("Enter the value: "))
index = -1
for i in range(len(values)):
    if values[i] == x:
        index = i
        break
print(index)
'''
'''
values = [5, 4, 9, 12]
summ=0

for i in range(len(values)): 
        summ = summ +values[i]
print(summ)
print(summ/len(values))

#min &max
print(min(values))
print(max(values))
'''

'''
value1 = [51, 14, 91, 12]
maxx=value1[0]       
for i in range(len(value1)):
    if value1[i]> maxx:
        maxx = value1[i]
        i+=1
print(maxx)

minn =value1[0]
for i in range(len(value1)):
    if value1[i]< minn:
        minn = value1[i]
        i+=1
print(minn)
'''
'''
value1 =[1,2,3,4,5,6,7,8,9,10]

for i in range(len(value1)):
    if value1[i] %2 != 0:
        print(value1[i])
        i+=1
        
       
value2 = [-1, 2, -3, 5, -4]

for i in range (len(value2)):
    if value2[i] < 0:
        value2[i] = 0
        i+=1
print (value2)
'''


'''
values =[2, 3, 4, 6, 1, 0]
target= 7

for i in range (len(values)):
    for j in range(i+1, len(values)):
       if values[i]+(values[j]) == target:
          print(values[i], values[j])
'''         
'''
# how many times apper in a list
listt = [1, 2, 2, 5, 4,5,3,5,4]
num= int(input("Enter a number: "))
count =0
for i in listt:
    if i == num:
        count+=1
print(count)
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

