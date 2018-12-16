import math

file = open("input.txt", "r")
lines = file.readlines()
grid = {}
points = list()
regionIndicator = 0
maxX = 0
maxY = 0
totals = {"#": 0}

for line in lines:
    items = line.strip().split(", ")
    x = int(items[0])
    y = int(items[1])

    points.append([x, y, regionIndicator])

    totals[regionIndicator] = 0

    if maxX < x:
        maxX = x

    if maxY < y:
        maxY = y

    try:
        grid[y][x] = regionIndicator
    except:
        grid[y] = {}
        grid[y][x] = regionIndicator

    regionIndicator += 1

def pointDistance(x, y):
    total = 0
    for point in points:
        total += math.fabs(x - point[0]) + math.fabs(y - point[1])
    if total < 10000:
        return "#"
    else:
        return "."

for i in range(maxY + 20):
    x = ""
    for j in range(maxX + 20):
        try:
            grid[i][j] = pointDistance(i, j)
        except:
            grid[i] = {}
            grid[i][j] = pointDistance(i, j)

        if pointDistance(i, j) != ".":
            totals[pointDistance(i, j)] += 1

for x in range(maxX + 19):
    if grid[0][x] != ".":
        totals[grid[0][x]] = 0
    if grid[maxY + 19][x] != ".":
        totals[grid[maxY + 19][x]] = 0
for y in range(maxY + 19):
    if grid[y][0] != ".":
        totals[grid[y][0]] = 0
    if grid[y][maxX + 19] != ".":
        totals[grid[y][maxX + 19]] = 0

max = 0
for x in totals:
    if totals[x] > max:
        max = totals[x]

print(max)
