with open("input.txt", "r") as f:
    file_input = f.readlines()

for i, line in enumerate(file_input):
    file_input[i] = line.split()[1:]

total = 1
for i, time in enumerate(file_input[0]):
    counter = 0
    time = int(time)
    distance = int(file_input[1][i])
    for milisecond in range(time+1):
        if milisecond * (time - milisecond) > distance:
            counter += 1
    if counter != 0:
        total *= counter

print(total)
