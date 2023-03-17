rowsAndColumns = input("enter the number of columns and rows ")
columns, rows = rowsAndColumns.split()
print(f'{columns =}, {rows = }')

labyrinth = [[input() for _ in range(0, int(columns))] for _ in range(0, int(rows))]

for row in labyrinth:
    for el in row:
        print(f'{el: ^5}', end="     ")
    print()
    print()

direction = input("Enter the initial direction ")

column = 0
row = 0

mirrorDict = {
    "/": [[row - 1, column, 'upside'], [row + 1, column, 'downward'], [row, column - 1, 'to the left'],
          [row, column + 1, 'to the right']],
    '\\': [[row + 1, column, 'downward'], [row - 1, column, 'upside'], [row, column + 1, 'to the right'],
           [row, column - 1, 'to the left']],
    ".": [[row, column + 1, 'to the right'], [row, column - 1, 'to the left'], [row + 1, column, 'downward'],
          [row - 1, column, 'upside']]
}
print(mirrorDict)
directionDict = {'to the right': 0, 'to the left': 1, 'downward': 2, 'upside': 3}

while True:
    if row < 0 or column < 0 or row >= int(rows) or column >= int(columns):
        print(f'The ray is out of the system {row = }, {column = }')
        break
    print(f'info before {row = }, {column = }, {direction = }')
    a, b, direction = mirrorDict[labyrinth[row][column]][directionDict[direction]]
    row = row + a
    column = column + b
    print(f'{row = }, {column = }, {direction}')
