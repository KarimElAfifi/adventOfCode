with open ("day3/batteryInput.txt", "r") as file:
    battery = file.readlines()

def find_highest_batteryCombination(battery):
    total = 0

    # this is just a safe guard to ensure we only process 
    # lines with at least 12 digits.
    # But here, it is optional, so its not "necessary"
#----------------------------------------
    for line in battery:
        line = line.strip()

        if not line or len(line) < 12:
            continue
        
        remove_count = len(line) - 12
#----------------------------------------

        stack = []
        
        for digit in line:
            # Remove smaller digits if the next digit is larger
            while stack and remove_count > 0 and stack[-1] < digit:
                stack.pop()
                remove_count -= 1
            stack.append(digit)
        
        # If we still need to remove digits, remove from the end
        while remove_count > 0:
            stack.pop()
            remove_count -= 1
        
        # join fucntion to put the digits together
        # then convert to integer
        # finally add to total
        joltage = int(''.join(stack))
        total += joltage

    return total

print(find_highest_batteryCombination(battery))


