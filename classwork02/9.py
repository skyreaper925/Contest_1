with open("input.txt", "r", encoding='utf-8') as fin:
    text = fin.readlines()
    text = [line.split() for line in text]
    sum9 = [];
    sum10 = [];
    sum11 = []
    for i in range(len(text)):
        if int(text[i][2]) == 9:
            sum9.append(int(text[i][3]))

        elif int(text[i][2]) == 10:
            sum10.append(int(text[i][3]))

        elif int(text[i][2]) == 11:
            sum11.append(int(text[i][3]))

    print(sum(sum9) / len(sum9), sum(sum10) / len(sum10), sum(sum11) / len(sum11))