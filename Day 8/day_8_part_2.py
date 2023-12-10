from math import lcm

with open("input.txt", "r") as f:
    file_input = f.readlines()

directions = file_input[0].strip()
nodes = {}
start_nodes = {} # this is stored in format "node ending with A : time it takes to end with Z"

for i, line in enumerate(file_input[2:]):
    line = line.strip().split(" = ")
    left, right = line[1].strip("()").split(", ")
    nodes[line[0]] = (left, right)
    if line[0][2] == "A":
        start_nodes[line[0]] = None

for node in start_nodes.copy().keys():
    current_node = node
    step = 0
    while current_node[2] != "Z":
        direction = directions[step % len(directions)]
        if direction == "L":
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]
        step += 1
    start_nodes[node] = step

# works out the LCM
values = list(start_nodes.values())
count = values[0]
for value in values[1:]:
    count = lcm(count, value)

print(count)