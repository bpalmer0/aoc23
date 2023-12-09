from typing import List


def predict(seq: List[int]) -> int:
    print(f"Predicting for {seq}")
    differences = [seq]
    current = seq
    while not all(list(map(lambda n: n == 0, current))):
        diff = []
        for i, num in enumerate(current):
            if i == 0:
                continue
            diff.append(num - current[i - 1])
        differences.append(diff)
        current = diff
    print(f"Found differences")
    print(differences)
    differences[-1].append(0)
    for i in range(len(differences) - 2, -1, -1):
        current = differences[i]
        below = differences[i + 1]
        current.append(current[-1] + below[-1])
    print(differences)
    prediction = differences[0][-1]
    print(f"Prediction: {prediction}")
    return prediction


def main():
    with open("input") as f:
        lines = f.read().split("\n")
    sequences = [
        [int(num) for num in line.strip().split(" ") if num != ""]
        for line in lines[:-1]
    ]
    print(sequences)
    predictions = [predict(seq) for seq in sequences]
    print(f"Sum of predictions: {sum(predictions)}")


if __name__ == "__main__":
    main()
