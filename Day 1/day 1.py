import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

for x in range(len(input)):
    input[x] = input[x].strip()


def part1():
    total = 0
    for entry in input:
        # Regex for finding all numbers
        numbers = re.findall("/d", entry)
        total += int(numbers[0] + numbers[-1])
    print(total)


def part2():
    total = 0
    word_to_int = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for entry in input:
        # Finds all word numbers in addition to integers
        numbers = re.findall("(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))", entry)
        # Convert words to integers
        if numbers[0] in word_to_int:
            numbers[0] = word_to_int[numbers[0]]
        if numbers[-1] in word_to_int:
            numbers[-1] = word_to_int[numbers[-1]]
        total += int(str(numbers[0]) + str(numbers[-1]))
    print(total)


part1()
part2()