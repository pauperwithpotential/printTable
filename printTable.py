tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    colWidths = [0] * len(tableData)                             # [0, 0, 0]
    for i in range(len(colWidths)):                              # range[0, 3]
        colWidths[i] = max(len(j) for j in tableData[i])         # get the max str len
        
    for x in range(len(table[0])):                               # 
        for y in range(len(table)):                              # 
            print(table[y][x].rjust(colWidths[y]), end = ' ')    # print with rjust using stored values from colWidths
        print()                                                  # print a new line

printTable(tableData)
