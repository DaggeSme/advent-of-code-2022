with open('input.txt') as f:
    contents = f.read()


sumlist = []
z = 0
x = contents.split("\n\n")
for line in x:
    line2 = line.replace("\n", "+")
    sumlist.append(eval(line2))
    if eval(line2) > z:
        z = eval(line2)
print("Top")
print(z)
print("======")

sumlist.sort()
while len(sumlist) > 3:
    sumlist.pop(0)
print("Top 3 total")
print(sum(sumlist))
print("======")



input('Press ENTER to exit')