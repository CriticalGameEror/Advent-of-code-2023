"""Day 4 part 2 solution for advent of code 2023"""

with open("input.txt", "r", encoding="utf-8") as f:
    file_input = f.readlines()

for i, line in enumerate(file_input):
    line = line.strip().split("|")
    line[0] = line[0].strip().split(" ")
    line[1] = line[1].strip().split(" ")
    file_input[i] = line




stack = [] # this contains all queued copies
card_results = {} # this contains the results of each card, keys stored as their number-1
total_cards = 0
for i, card in enumerate(file_input):
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
    card_results[i+1] = matches
    # highlights the number of instances made just from the originals
    total_cards += matches+1 # plus 1 because it includes the current card
    # adds the copies to the stack
    for x in range(1, matches+1):
        stack.append(i+x+1)

while len(stack) != 0:
    card = stack.pop()
    result = card_results[card]
    for x in range(1, result+1):
        stack.append(card+x)
    total_cards += result

print(total_cards)
