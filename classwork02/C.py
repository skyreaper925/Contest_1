with open("input.txt", "r") as fin:
    n = int(fin.read(1))
    # print(fin.readlines())
    print(Counter(fin.readlines().most_common([n]))
    # fin.close()