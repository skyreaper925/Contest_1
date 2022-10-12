with open("input.txt", "r", encoding='utf-8') as fin:
    text = fin.readlines()
    text = [line.split() for line in text]
    maximum = 0;
    school_maximum = set()
    for i in range(len(text)):
        if int(text[i][3]) >= maximum:
            maximum = int(text[i][3])
            school_maximum.add(text[i][2])

    school_maximum = sorted(school_maximum)
    print(*school_maximum)