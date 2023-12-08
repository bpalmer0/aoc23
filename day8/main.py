def main():
    with open("input") as f:
        lines = f.read().split("\n")
    directions = lines[0]
    node_strs = lines[2:-1]
    nodes = {}
    for node_str in node_strs:
        split = node_str.split(" = ")
        name = split[0]
        print(f"{name=}")
        destinations = split[1][1:-1].split(", ")
        print(f"{destinations}")

        nodes[name] = destinations
    print(directions, nodes)

    current_node = "AAA"
    steps = 0
    while current_node != "ZZZ":
        next = nodes[current_node]
        direction = directions[steps % len(directions)]
        if direction == "R":
            current_node = next[1]
        else:
            current_node = next[0]
        steps += 1
    print(f"ZZZ reached in {steps} steps")


if __name__ == "__main__":
    main()
