array = [[2, 8, 7, 1, 2, 7, 6, 2, 4, 8, 6],
         [2, 8, 7, 1, 2, 7, 6, 2, 4, 8, 6],
         [2, 8, 7, 1, 2, 7, 6, 2, 4, 8, 6],
         [2, 8, 7, 1, 2, 7, 6, 2, 4, 8, 6]
         ]


def sort_by_row(array, sort_by_index, reverse=False):
    for rows in range(len(array[0])):
        for columns in range(len(array)):
            if reverse == True:
                condtion = array[sort_by_index][rows] > array[sort_by_index][columns]
            else:
                condtion = array[sort_by_index][rows] < array[sort_by_index][columns]
            if condtion:
                for i in range(len(array)):
                    temp = array[i][rows]
                    array[i][columns] = array[i][rows]
                    array[i][rows] =temp
    return array


for x in sort_by_row(array, 3,reverse=True):
    print(x)
    pass
