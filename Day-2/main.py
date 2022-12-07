with open('input.txt') as f:
    contents = f.read()

score = 0
#A = rock 1
#B = paper 2
#C = scissors 3
#X = Lose
#Y = draw
#Z = win

x = contents.split("\n")
for line in x:
    if line.__contains__("X") and line.__contains__("A"):
        #Lose +0 lose with siccors + 3
        score += 3
    elif line.__contains__("X") and line.__contains__("B"):
        #Lose +0 lose with rock + 1
        score += 1
    elif line.__contains__("X") and line.__contains__("C"):
        #Lose +0 lose with paper + 2
        score += 2
    elif line.__contains__("Y") and line.__contains__("A"):
        #Draw +3 draw with rock + 1
        score += 4
    elif line.__contains__("Y") and line.__contains__("B"):
        #Draw +3 draw with paper + 2
        score += 5
    elif line.__contains__("Y") and line.__contains__("C"):
        #Draw +3 draw with siccors + 3
        score += 6
    elif line.__contains__("Z") and line.__contains__("A"):
        #Win +6 win with paper + 2
        score += 8
    elif line.__contains__("Z") and line.__contains__("B"):
        #Win +6 win with siccors + 3
        score += 9
    elif line.__contains__("Z") and line.__contains__("C"):
        #Win +6 win with rock + 1
        score += 7
    

print(score)








input('Press ENTER to exit')