file=open("statments.txt","r")
print(file.readline())
lines=[]
for line in file:
    print(line)
    lines.append(line)
    print(lines)
file.close()