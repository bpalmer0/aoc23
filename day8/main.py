from math import lcm


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

    starting_nodes = [node for node in nodes.keys() if node.endswith("A")]
    print(f"{starting_nodes=}")
    ending_nodes = [node for node in nodes.keys() if node.endswith("Z")]
    print(f"{ending_nodes=}")
    periods = []
    for starting_node in starting_nodes:
        steps = 0
        z_node_steps = []
        current_node = starting_node
        while steps <= 100000:
            next = nodes[current_node]
            direction = directions[steps % len(directions)]
            if direction == "R":
                next_node = next[1]
            else:
                next_node = next[0]
            steps += 1
            if next_node.endswith("Z"):
                z_node_steps.append((steps, next_node))
            current_node = next_node
        print(f"Starting node {starting_node} reached Z nodes at {z_node_steps}")
        differences = []
        for i, (steps, node) in enumerate(z_node_steps):
            if i == 0:
                continue
            differences.append(steps - z_node_steps[i - 1][0])
        print(f"Differences {differences}")
        periods.append(differences[-1])
    steps = lcm(*periods)
    print(f"All destination nodes reached in {steps} steps")


if __name__ == "__main__":
    main()
