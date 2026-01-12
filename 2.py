import re

with open("IDs.txt", "r") as file:
    id = file.readline()
    strID = id.split(',')

# finding invalid IDs 
# safing them in invalid_ids list
# adding their values to sum
def find_invalid_ID(strID):
    invalid_ids = []

    for i in strID:
        i = i.strip()

        numRange = re.search(r'(\d+)-(\d+)', i)
        
        minNum = int(numRange.group(1))
        maxNum = int(numRange.group(2))

        for x in range(minNum, maxNum + 1):
            if re.fullmatch(r'(.+?)\1+', str(x)):
                invalid_ids.append(x)

    return sum(invalid_ids)

print(find_invalid_ID(strID))