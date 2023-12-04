"""Day 4 part 1 solution for advent of code 2023"""

with open("input.txt", "r", encoding="utf-8") as f:
    file_input = f.readlines()

for i, line in enumerate(file_input):
    line = line.strip().split("|")
    line[0] = line[0].strip().split(" ")
    line[1] = line[1].strip().split(" ")
    file_input[i] = line

total = 0
for card in file_input:
    winning_set = set()
    current_set = set()
    for number in card[0][2:]: # starts iterating though the numbers from the 3rd element
        # ignores any empty elements from formatting
        if number == "":
            continue
        winning_set.add(number)
    for number in card[1]:
        # ignores any empty elements from formatting
        if number == "":
            continue
        current_set.add(number)
    matches = len(winning_set.intersection(current_set))
    if matches != 0:
        total += 2 ** (len(winning_set.intersection(current_set)) - 1)

print(total)
