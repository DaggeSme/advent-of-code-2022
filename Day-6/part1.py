with open('input.txt') as f:
    contents = f.read()
done = False


def dup(somelist):
    yes = False
    no = False
    e = range(0,len(somelist))
    for times in e:
        i = 0 + times + 1
        while i < len(somelist):
            if somelist[times] == somelist[i]:
                yes = True
            else:
                no = True
            i += 1
    if yes == False and no == True:
        return True
    else:
        return False


q = range(0,len(contents))
done = False
for times in q:
    if done == False:
        List = []
        List.append(contents[times])
        List.append(contents[times+1])
        List.append(contents[times+2])
        List.append(contents[times+3])
        if dup(List) == True:
            done = True
            print("Part1:")
            print(times+4)
q = range(0,len(contents))
done = False
for times in q:
    if done == False:
        List = []
        List.append(contents[times])
        List.append(contents[times+1])
        List.append(contents[times+2])
        List.append(contents[times+3])
        List.append(contents[times+4])
        List.append(contents[times+5])
        List.append(contents[times+6])
        List.append(contents[times+7])
        List.append(contents[times+8])
        List.append(contents[times+9])
        List.append(contents[times+10])
        List.append(contents[times+11])
        List.append(contents[times+12])
        List.append(contents[times+13])
        if dup(List) == True:
            done = True
            print("Part2:")
            print(times+14)
