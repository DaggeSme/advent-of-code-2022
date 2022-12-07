with open('input.txt') as f:
    contents = f.read()
x = contents.split("\n\n")
x.pop(1)
templist = []
list = []
for lines in x:
    y = lines.split("\n")
    y.pop(len(y) - 1)
    y.reverse()
    k = range(1, 35, 4 )
    for n in k:
        for lines in y:
            if lines[n] != ' ':
                templist.append(lines[n])
        list.append(templist)
        templist = []


p = contents.split("\n\n")
p.pop(0)
for lines in p:
    r = lines.split("\n")
    for lines in r:
        p = lines.split(' ')
        p.remove("move")
        p.remove("from")
        p.remove("to")
        o = range(0, int(p[0]))
        for times in o:
            list[int(p[2])-1].append(list[int(p[1])-1][len(list[int(p[1])-1])-1])
            list[int(p[1])-1].pop(len(list[int(p[1])-1])-1)
for lines in list:
    print(lines[len(lines)-1])


