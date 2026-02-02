with open ("day4/paperInput.txt", "r") as file:
    paper = [line.strip() for line in file.readlines()]


def checkHowMuchPaper(paper):
    countThePaper = 0
    

    neighborsOffsets = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

    for row in range(len(paper)):
        for column in range(len(paper[row])):
            neighbors = 0
            if paper[row][column] == "@":
                for offset in neighborsOffsets:
                    neighborRow = row + offset[0]
                    neighborColumn = column + offset[1]

                    if 0 <= neighborRow < len(paper) and 0 <= neighborColumn < len(paper[row]):
                        if paper[neighborRow][neighborColumn] == "@":
                            neighbors += 1

                if neighbors < 4:
                    countThePaper += 1

    return countThePaper

print(checkHowMuchPaper(paper))


