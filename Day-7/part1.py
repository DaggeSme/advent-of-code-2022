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

with open('Day-7/input.txt') as f:
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
print(list)

#if list contains dir. go to dir. if that dir conatins dir. go to dir and so forth. if not calculate sum then back out. do the rest until done



""" for lines in list:
    if lines.__contains__("$"):
        dest_dir = lines[0][:lines[0].rindex('/')]
        dest_dir = dest_dir[:dest_dir.rindex('/')+1]
        replace_dir = lines[0][:lines[0].rindex('/')]
        replace_dir = replace_dir[dest_dir.rindex('/')+1:]
        try:
            list[find(list, dest_dir, 0)][list[find(list, dest_dir, 0)].index("dir " + replace_dir)]=mysum(lines)
        except:
            pass """



""" sum=0
for lines in list:
    print(lines)
    print(mysum(lines))
    file = open('Failed.txt', 'a')
    file.write(str(lines)+"\n")
    file.write(str(mysum(lines))+"\n")
    file.close()
    if mysum(lines) < 100000:
        sum+=mysum(lines) 
print("SUM!")
print(sum) """