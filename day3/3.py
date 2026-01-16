with open ("day3/batteryInput.txt", "r") as file:
    battery = file.readlines()

def find_highest_batteryCombination(battery):

    total = 0

    for line in battery:
        line = line.strip()

        if not line or len(line) < 2:
            continue

        max_joltage = 0
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line)):
                joltage = int((line[i]) * 10 + int(line[j]))

                max_joltage = max(max_joltage, joltage)

        total += max_joltage

    return total

print(find_highest_batteryCombination(battery))


