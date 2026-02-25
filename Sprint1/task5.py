import sys

def solution():
    matrix = []

    lenght_text = int(input())
    text = sys.stdin.readline().rstrip()

    arr_words = text.split()

    if len(arr_words) == 1:
        print(arr_words[0])
        print(len(arr_words[0]))
        return

    if days == 2 and temps[0]!=temps[1]:
        print(1)
        return

    result = 0
    len_temps = len(temps)
    for k, v in enumerate(temps):
        if k == 0 and v > temps[1]:
            result += 1
        elif k == len_temps - 1 and temps[k-1] < v:
            result += 1
        elif temps[k-1] < v and temps[k+1] < v:
            result += 1

    print(result)
if __name__ == '__main__':
    solution()
