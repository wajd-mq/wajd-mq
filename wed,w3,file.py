'''
infile= open("C:/Users/DELL/Desktop/data.txt", "r")

line1 = infile.readline()
print(line1)

line2 = infile.readline()
print(line2)


infile.close()
'''
'''
infile= open("C:/Users/DELL/Desktop/data.txt", "r")

line= infile.readline()
noLinnes= 1
while line !="":
    print(line)
    noLinnes +=1
    line= infile.readline()
infile.close()
'''
'''
infile= open("C:/Users/DELL/Desktop/data.txt", "r")

lines= infile.readlines()
print(lines)
print(len(lines))



for i in range(len(lines)):
    lines[i] = int(lines[i].strip())
print(lines)
print(sum(lines)/ len(lines))
print(max(lines))


infile.close()
'''
'''
infile= open("C:/Users/DELL/Desktop/data.txt", "r")
print(infile.read())
infile.close()
'''
'''
infile= open("C:/Users/DELL/Desktop/data.txt", "r")
lines= infile.read().split("\n")
print(lines)
infile.close()
'''
'''
infile= open("C:/Users/DELL/Desktop/data.txt", "w")
infile.write("Hello Nafath\nFrom Wajd")

infile.close()
'''

infile= open("C:/Users/DELL/Desktop/data.txt", "w")
print("Hello Nafath\nFrom Wajd", file=infile)

infile.close()