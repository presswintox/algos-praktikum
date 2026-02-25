import sys

def solution():
    matrix = []

    count_lines = int(input())
    count_columns = int(input())

    for lines in range(count_lines):
        line = sys.stdin.readline().rstrip()
        line = line.split()
        matrix.append(line)

    search_num_x = int(input())
    search_num_y = int(input())


    if count_columns == 1 and count_lines == 1:
        print()
        return

    result = []

    if count_lines - 1 > search_num_x >= 0 :
        result.append(int(matrix[search_num_x + 1][search_num_y]))

    if count_lines - 1 >= search_num_x > 0 :
        result.append(int(matrix[search_num_x - 1][search_num_y]))

    if count_columns - 1 > search_num_y >= 0 :
        result.append(int(matrix[search_num_x][search_num_y + 1]))

    if count_columns - 1 >= search_num_y > 0 :
        result.append(int(matrix[search_num_x][search_num_y - 1]))

    result.sort()
    print(*result)
    return

if __name__ == '__main__':
    solution()
