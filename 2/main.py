with open("input.txt", 'r') as f:
    instructions = [instruction.strip().split(" ") for instruction in f.readlines()]
    horizontal = 0
    depth = 0
    for (direction, x) in instructions:
        match direction:
            case "forward":
                horizontal += int(x)
            case "up":
                depth -= int(x)
            case "down":
                depth += int(x)
    print("Part1 :", horizontal * depth)

with open("input.txt", 'r') as f:
    instructions = [instruction.strip().split(" ") for instruction in f.readlines()]
    horizontal = 0
    depth = 0
    aim = 0
    for (direction, x) in instructions:
        match direction:
            case "forward":
                horizontal += int(x)
                depth += int(x) * aim
            case "up":
                aim -= int(x)
            case "down":
                aim += int(x)
    print("Part2 :", horizontal * depth)

