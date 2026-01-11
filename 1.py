with open ("rotations.txt", 'r') as file:
    rotations = file.readlines()

def counting_dial_on_zero(rotations):
    #starting position
    pos = 50
    #counter for how many times it lands on 0
    count = 0
    for rotation in rotations:
        rotation = rotation.strip()
        direction = rotation[0]
        steps = int(rotation[1:])

        for x in range(steps):
            if pos == 0:
                count += 1
            if direction == 'R':
                pos = (pos + 1) % 100
            elif direction == 'L':
                pos = (pos - 1) % 100


        # if direction == 'R':
        #     if pos + steps > 99:
        #         count += 1
        #     pos = (pos + steps) % 100
            
        #     # Wrap around if exceeds 99
        # elif direction == 'L':
        #     if pos - steps < 0:
        #         count += 1
        #     pos = (pos - steps) % 100
        # if pos == 0:
        #     count += 1
    return count

print(counting_dial_on_zero(rotations))