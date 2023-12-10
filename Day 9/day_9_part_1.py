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
    predicted = 0
    difference = find_diference(line)
    predicted += difference[-1] + int(line[-1])
    while len(Counter(difference)) != 1:
        difference = find_diference(difference)
        predicted += difference[-1]
    total += predicted

print(total)