with open('input.txt') as f:
    contents = f.read()
done = False


def dup(somelist):
    yes = False
    no = False
    e = range(0,len(somelist))
    for times in e:
        #print(times)
        i=len(somelist)-1
        while i < len(somelist)-1:
            i+=1
            print("times=",times)
            print("i=",i)
            print(somelist[times],somelist[i])
            if somelist[times] == somelist[i]:
                yes = True
            else:
                no = True
    if yes == False and no == True:
        return False
    else:
        return True

q = range(0,len(contents))
for times in q:
    if done == False:
        List = []
        List.append(contents[times])
        List.append(contents[times+1])
        List.append(contents[times+2])
        List.append(contents[times+3])
        if dup(List) != True:
            done = True
            print(times+4)