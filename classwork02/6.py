with open("input.txt", "r", encoding='utf-8') as fin:
    a = fin.readlines()
    a = [line.split() for line in a]
    max9 = 0;
    max10 = 0;
    max11 = 0
    for i in range(len(a)):
        if int(a[i][2]) == 9 and int(a[i][3]) > max9:
            max9 = int(a[i][3])

        elif int(a[i][2]) == 10 and int(a[i][3]) > max10:
            max10 = int(a[i][3])

        elif int(a[i][2]) == 11 and int(a[i][3]) > max11:
            max11 = int(a[i][3])

    print(max9, max10, max11)