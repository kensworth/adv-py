arr = [[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12],
 [13, 14, 15, 16]]

def print_arr(arr):
    for line in arr:
        print line
    print

def rotate(arr):
    length = len(arr) - 1
    for x in range(len(arr) // 2):
        for y in range(length - (2 * x)):
            temp1 = arr[x + y][x]
            temp2 = arr[length - x][x + y]
            temp3 = arr[length - x - y][length - x]
            temp4 = arr[x][length - x - y]
            #  print temp1, temp2, temp3, temp4
            arr[x + y][x] = temp4
            arr[length - x][x + y] = temp1
            arr[length - x - y][length - x] = temp2
            arr[x][length - x - y] = temp3
            # print arr[x + y][x], arr[length - x][x + y], arr[length - x][length - x - y], arr[x][length - x - y]

print_arr(arr)
rotate(arr)
print_arr(arr)
