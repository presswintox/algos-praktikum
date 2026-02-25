import sys

WIN = 'WIN'
FAIL = 'FAIL'

def solution():
    line = sys.stdin.readline().rstrip()
    a, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)

    if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        print(WIN)
        return

    if a % 2 != 0 and b % 2 != 0 and c % 2 != 0:
        print(WIN)
        return

    print(FAIL)
    return

if __name__ == '__main__':
    solution()
