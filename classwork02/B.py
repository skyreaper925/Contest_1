with open("input.txt", "r") as fin:
    with open("output.txt", "w") as fout:
        n = int(fin.read(1))
        i = 1
        while fin.readline(i):
            k = (i - 1) % n
            fout.write(str(k) + " " + str(fin.readline(i)) + '\n')
            # print(str(fin.readline(i)))
            i += 1
