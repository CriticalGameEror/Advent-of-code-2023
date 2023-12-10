with open("input.txt", "r") as f:
    file_input = f.readlines()

directions = file_input[0].strip()
nodes = {}

for i, line in enumerate(file_input[2:]):
    line = line.strip().split(" = ")
    left, right = line[1].strip("()").split(", ")
    nodes[line[0]] = (left, right)

current_node = "AAA"
step = 0
while current_node != "ZZZ":
    direction = directions[step % len(directions)]
    if direction == "L":
        current_node = nodes[current_node][0]
    else:
        current_node = nodes[current_node][1]
    step += 1

print(step)