with open('input.txt') as f:
    contents = f.read()

value = 0
found = False
lines = contents.split("\n")
print(len(lines))
while len(lines) >= 3:
    found = False
    for element in lines[0]:
        try:
            if lines[1].__contains__(element) == True and lines[2].__contains__(element) and found == False:
                found = True
                if element.islower() == True:
                    x = (ord(element) - 96)
                    value = value + x
                    print(element)
                    print(x)
                    lines.pop(0)
                    lines.pop(0)
                    lines.pop(0)
                else:
                    x =(ord(element) - 38)
                    value = value + x
                    print(element)
                    print(x)
                    lines.pop(0)
                    lines.pop(0)
                    lines.pop(0)
        except:
            print("DONE!")
    
print("=========")
print(value)
input('Press ENTER to exit')



