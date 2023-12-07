with open("input.txt", "r") as f:
    file_input = f.readlines()

for i, line in enumerate(file_input):
    file_input[i] = line.replace(" ", "").strip().split(":")[1]

total = 0
time = int(file_input[0])
distance = int(file_input[1])
for milisecond in range(time+1):
    if milisecond * (time - milisecond) > distance:
        total += 1

print(total)