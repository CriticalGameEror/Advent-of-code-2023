with open("input.txt", "r") as f:
    input = f.readlines()

for line in range(len(input)):
    input[line] = input[line].strip()

non_symbols = ["1","2","3","4","5","6","7","8","9","0","."]
symbol_cords = set() # stored in "(x,y)" format
numbers_cords = {} # stored as "(x,y):number"

is_number = False
current_number = ""

# first find the coords of all the symbols and the cords ranges of the numbers
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] not in non_symbols:
            symbol_cords.add((x,y))
            if is_number == True:
                is_number = False
                for cord in current_number_cords:
                    numbers_cords[cord] = int(current_number)
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
for symbol in symbol_cords:
    for y in range(-1,2):
        for x in range(-1,2):
            if (symbol[0]+x, symbol[1]+y) in numbers_cords:
                # add the value of the number at those cords
                total += int(numbers_cords[(symbol[0]+x, symbol[1]+y)])

                # now remove that number from the dictionary
                pointer = symbol[0]+x
                while (pointer, symbol[1]+y) in numbers_cords:
                    pointer -= 1
                pointer += 1
                while (pointer, symbol[1]+y) in numbers_cords:
                    numbers_cords.pop((pointer, symbol[1]+y))
                    pointer += 1

print(total)