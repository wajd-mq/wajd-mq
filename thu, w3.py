'''
infile = open("C:/Users/DELL/Desktop/waj.txt", "r")

text = infile.read()
wordList= text.split()

print("The words: ",wordList)
print("number of words: ", len(wordList))


#way 1
rep =0
for i in range(len(wordList)):
    if wordList[i].lower().strip() == "the":
        rep=rep+1
print(rep)

#way2 
for i in range(len(wordList)):
    wordList[i]=wordList[i].lower().strip()
theCount = wordList.count("the")
print(theCount)


lisTheIndex = []
for i in range(len(wordList)):
    if wordList[i] == "the":
        lisTheIndex.append(i)
        
for index in range(len(lisTheIndex)):
    
    if index == len(lisTheIndex) -1:
        print(wordList[lisTheIndex[index]: ])
    else:
        print(wordList[lisTheIndex[index]:lisTheIndex[index+1]])
        
        
       
infile.close()
'''
###

'''
amount= 600
balance= 300

if amount > balance:
    raise ValueError("Amount exceeds balance")
'''
'''
try:
    infile = open("C:/Users/DELL/Desktop/waj.txt", "r")
    line = infile.readline()
    print(line)
    print(5/0)
    
except IOError:
    print("Could not open file.")
except Exception as exceptObj:
    print("Error:", str(exceptObj))
    
'''

inputOK= False
while (inputOK == False):
    try:
        num = input("Enter a number: ")
        num = float(num)
        
        inputOK= True
        
    except ValueError:
        print("Non-numeric type entered '%s'" %num)
        
num = num*2
print(num)