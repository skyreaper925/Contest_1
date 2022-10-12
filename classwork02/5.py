with open("input.txt", "r") as fin:
    a = fin.read().splitlines()
    a.reverse()
    for line in a:
        print(line[::-1], end = '\n')