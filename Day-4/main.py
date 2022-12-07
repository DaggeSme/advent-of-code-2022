with open('input.txt') as f:
    contents = f.read()
sum = 0
sum2 = 0
x = contents.split("\n")
for lines in x:
    q = lines.split(",")
    result_3 = [item.split('-') for item in q]
    result_3_flat = [item for l in result_3 for item in l]
    test = []
    test2 = []
    k = range(int(result_3_flat[0]),int(result_3_flat[1]) + 1)
    for l in k:
        test.append(l)
    r = range(int(result_3_flat[2]),int(result_3_flat[3]) + 1)
    for l in r:
        test2.append(l)
    if all(elem in test  for elem in test2) or all(elem in test2  for elem in test):
        sum = sum + 1
    if any(elem in test  for elem in test2) or any(elem in test2  for elem in test):
        sum2 = sum2 + 1

print("part 1:")
print(sum)
print("part 2:")
print(sum2)
input("Press enter to exit!")