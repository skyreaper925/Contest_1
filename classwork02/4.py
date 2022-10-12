with open("input.txt", "r") as fin:
    a = fin.readlines()
    a = [line.rstrip() for line in a]
    for i in range(len(a) - 1, -1, -1):
        print(a[i])