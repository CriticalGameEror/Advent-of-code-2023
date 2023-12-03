import re

f = open("input.txt", "r")
input = f.readlines()
f.close()

for length in range(len(input)):
    input[length] = input[length].strip()
    input[length] = re.split(": |, |; ", input[length]) # splits the list at any special characters identified in the input

max_red = 12
max_green = 13
max_blue = 14

def part1():
    total = 0
    for game in range(len(input)):
        impossible_flag = False
        for pull in range(1, len(input[game])):
            instance = input[game][pull]
            if "red" in instance:        
                instance = instance.strip("red")
                if int(instance) > max_red:
                    impossible_flag = True
            elif "green" in instance:
                instance = instance.strip("green")
                if int(instance) > max_green:
                    impossible_flag = True
            elif "blue" in instance:
                instance = instance.strip("blue")
                if int(instance) > max_blue:
                    impossible_flag = True
        
        if not impossible_flag:
            total += game + 1

    print(total)

def part2():
    total = 0
    for game in range(len(input)):
        instance_max_red = 0
        instance_max_green = 0
        instance_max_blue = 0
        for pull in range(1, len(input[game])):
            instance = input[game][pull]
            if "red" in instance:        
                instance = instance.strip("red")
                if int(instance) > instance_max_red:
                    instance_max_red = int(instance)
            elif "green" in instance:
                instance = instance.strip("green")
                if int(instance) > instance_max_green:
                    instance_max_green = int(instance)
            elif "blue" in instance:
                instance = instance.strip("blue")
                if int(instance) > instance_max_blue:
                    instance_max_blue = int(instance)
        
        total += (instance_max_red * instance_max_green * instance_max_blue)

    print(total)

part1()
part2()
