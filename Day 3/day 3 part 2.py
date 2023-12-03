with open("input.txt", "r") as f:
    input = f.readlines()

for line in range(len(input)):
    input[line] = input[line].strip()

non_symbols = ["1","2","3","4","5","6","7","8","9","0","."]
gear = "*"
gear_cords = set() # stored in "(x,y)" format
numbers_cords = {} # stored as "(x,y):number"

is_number = False
current_number = ""

# first find the coords of all the gears and the cords ranges of the numbers
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == gear:
            gear_cords.add((x,y))
            if is_number == True:
                is_number = False
                for cord in current_number_cords:
                    numbers_cords[cord] = int(current_number)
        elif input[y][x] not in non_symbols:
            continue
        else:
            if input[y][x] not in "." and is_number == False:
                # tracks the position of the number
                current_number = input[y][x]
                current_number_cords = []
                current_number_cords.append((x,y))
                is_number = True
            elif input[y][x] not in "." and is_number == True:
                current_number += input[y][x]
                current_number_cords.append((x,y))
            elif input[y][x] == "." and is_number == True:
                is_number = False
                for cord in current_number_cords:
                    numbers_cords[cord] = int(current_number)

total = 0
for symbol in gear_cords:
    numbers_cords_copy = numbers_cords.copy() # this is needed as the changes to the numbers should not be saved
    adjacent_numbers = [] # the numbers around the gear symbol
    for y in range(-1,2):
        for x in range(-1,2):
            # might as well try to exit the loop as the symbol is not a valid gear if len is more than 2
            if len(adjacent_numbers) > 2:
                break
            if (symbol[0]+x, symbol[1]+y) in numbers_cords_copy:
                # add the value of the number at those cords
                adjacent_numbers.append(int(numbers_cords_copy[(symbol[0]+x, symbol[1]+y)]))
                # now remove that number from the copy dictionary
                pointer = symbol[0]+x
                while (pointer, symbol[1]+y) in numbers_cords_copy:
                    pointer -= 1
                pointer += 1
                while (pointer, symbol[1]+y) in numbers_cords_copy:
                    numbers_cords_copy.pop((pointer, symbol[1]+y))
                    pointer += 1
    # gets the gear ratio if there are exactly 2 adjacent numbers
    if len(adjacent_numbers) == 2:
        total += (adjacent_numbers[0] * adjacent_numbers[1])

print(total)