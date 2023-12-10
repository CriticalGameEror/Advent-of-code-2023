from collections import Counter

with open("input.txt", "r") as f:
    file_input = f.readlines()

for i, line in enumerate(file_input):
    line = line.strip().split()
    file_input[i] = line

def find_diference(sequence):
    new = []
    for number in range(0, len(sequence)-1):
        new.append(int(sequence[number+1]) - int(sequence[number]))
    return new

total = 0
for line in file_input:
    difference = find_diference(line)
    predicted = int(line[0]) - difference[0]
    flag = True # this flag is used as every other difference is added instead of taken away
    while len(Counter(difference)) != 1:
        difference = find_diference(difference)
        if flag == False:
            predicted -= difference[0]
        else:
            predicted += difference[0]
        flag = not(flag)
    total += predicted

print(total)