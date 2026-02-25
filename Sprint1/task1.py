import sys

def solution():
    line = sys.stdin.readline().rstrip()
    a, x, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    x = int(x)
    result = a*x**2+b*x+c
    print(result)
    return

if __name__ == '__main__':
    solution()
