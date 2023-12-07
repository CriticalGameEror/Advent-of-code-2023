from collections import Counter

with open("input.txt", "r") as f:
    file_input = f.readlines()

hands = {}
for line in file_input:
    line = line.strip().split(" ")
    hands[line[0]] = int(line[1])

# block below sorts each hand into each of the categories
hand_types = {"five_kind":[], "four_kind":[], "full":[], "three_kind":[], "two_pair":[], "one_pair":[], "high":[]}
for hand in hands.keys():
    count = Counter(hand)
    if len(count) == 1 or (len(count) == 2 and "J" in hand):
        hand_types["five_kind"].append(hand)
    elif len(count) == 2 or (len(count) == 3 and "J" in hand):
        if 4 in count.values():
            hand_types["four_kind"].append(hand)
        elif "J" in hand:
            if max(count.values()) + count["J"] >= 4:
                hand_types["four_kind"].append(hand)
            else:
                hand_types["full"].append(hand)
        else:
            hand_types["full"].append(hand)
    elif len(count) == 3 or (len(count) == 4 and "J" in hand):
        if 3 in count.values():
            hand_types["three_kind"].append(hand)
        elif "J" in hand:
            if max(count.values()) + count["J"] >= 3:
                hand_types["three_kind"].append(hand)
            else:
                hand_types["two_pair"].append(hand)
        else:
            hand_types["two_pair"].append(hand)
    elif len(count) == 4 or (len(count) == 5 and "J" in hand):
        hand_types["one_pair"].append(hand)
    else:
        hand_types["high"].append(hand)

# block below is for sorting the hands so higher weighted hands are given a higher rank in the same category
card_types = "AKQT987654321J"
sorting_order = dict(zip(card_types, range(50,35,-1)))
def convert_to_number(hand):
    temp = ""
    for letter in hand:
        temp += str(sorting_order[letter])
    return int(temp)

total = 0
position = 1
for key in reversed(hand_types.keys()):
    if len(hand_types[key]) == 0:
        continue
    elif len(hand_types[key]) == 1:
        total += position * hands[hand_types[key][0]]
        position += 1
    else:
        order = sorted(hand_types[key], key=convert_to_number)
        for hand in order:
            total += position * hands[hand]
            position += 1

print(total)
