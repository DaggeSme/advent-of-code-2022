def mysum(inlist):
    sum = 0
    for items in inlist:
        try:
            sum+=int(items)
        except:
            pass
    return sum
def find(inlist, infind, whatreturn):
    i=0
    for lines in inlist:
        if whatreturn == 0:
            try:
                int(lines.index(infind))
                return i
            except:
                pass
            i+=1
        else:
            try:
                return int(lines.index(infind))
            except:
                pass
            i+=1

with open('input.txt') as f:
    contents = f.read()
x = contents.split("\n")
list = []
templist = []
curdir = ""
lastdir = ""
for lines in x:
    if lines.__contains__("cd ") == True and lines.__contains__("..") == False: #and templist.__contains__(lines.split(' ')[2]) == False:
        list.append(templist)
        templist = []
        lastdir = lines.split(' ')
        if lines.__contains__("cd /"):
            curdir = "/"
        else:
            curdir= curdir + lines.split(' ')[2] + "/"
        templist.append(curdir)
    if lines.__contains__("cd .."):
        index = curdir.rindex('/')
        curdir = curdir[index:]
    if lines.__contains__("$") == False and lines.__contains__("dir") == False:
        templist.append(lines.split(' ')[0])
    elif lines.__contains__("$") == False and lines.__contains__("dir") == True:
        templist.append(lines)
list.append(templist)
list.pop(0)
list.reverse()
for lines in list:
    try:
        index = lines[0].rindex('/')
        test = lines[0][:index]
        index = test.rindex('/')+1
        final = test[index:]
        #print(lines)
        #print(test)
        #print(final)
    except:
        pass
        index = lines[0].rindex('/')
        test2 = lines[0][:index]
        index = lines[0].rindex('/')+1
        key = test2[index:]
        print(key)
    
    
    try:
        list[find(list, test,0)][list[find(list, test,0)].index("dir "+key)]=mysum(lines)
    except:
        pass



sum=0
for lines in list:
    #print(lines)
    #print(mysum(lines))
    if mysum(lines) > 100000:
        pass
    else:
        sum+=mysum(lines)
print("SUM!")
print(sum)