import sys

def solution():
    matrix = []

    num_lines = int(input())
    num_columns = int(input())

    for lines in range(num_lines):
        line = sys.stdin.readline().rstrip()
        line = [int(x) for x in line.split()]
        matrix.append(line)

    search_num_x = int(input())
    search_num_y = int(input())

    if num_columns == 1 and num_lines == 1:
        print()
        return

    if num_columns == 1:
        if search_num_x == 0:
            print(matrix[search_num_x + 1][0])
        elif search_num_x == num_lines - 1:
            print(matrix[search_num_x - 1][0])
        return

    if num_lines == 1:
        if search_num_y == 0:
            print(matrix[0][search_num_y + 1])
        elif search_num_y == num_columns - 1:
            print(matrix[0][search_num_y - 1])
        return

    result_indexes = {
        1:[search_num_x - 1,search_num_y],
        2:[search_num_x + 1,search_num_y],
        3:[search_num_x, search_num_y - 1],
        4:[search_num_x, search_num_y + 1]
    }


    if search_num_x == 0:
        del result_indexes[1]
    elif search_num_x == num_lines - 1:
        del result_indexes[2]

    if search_num_y == 0:
        del result_indexes[3]
    elif search_num_y == num_columns - 1:
        del result_indexes[4]
    res_array = [matrix[val[0]][val[1]] for val in result_indexes.values()]
    res_array.sort()
    print(*res_array)
    return

if __name__ == '__main__':
    solution()
