with open("input.txt", "r") as fin:
    a = fin.read().splitlines()
    a.reverse()
    for i in range(len(a) - 1, -1, -1):
        print(a[i][::-1])