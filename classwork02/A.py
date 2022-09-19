from itertools import zip_longest
with open("input.txt", "r") as f:
    a = []
    a = f.read().splitlines()
    x = len(a)
    while x:
        a[len(a) - x] = a[len(a) - x].split()
        x -= 1
    print(a)

    for i in range(len(a)):
        rez = zip_longest(a[i], fillvalue=0)
    print(rez)