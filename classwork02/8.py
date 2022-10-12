with open("input.txt", "r", encoding='utf-8') as fin:
    text = fin.readlines()
    text = [line.split() for line in text]
    text = sorted(text)
    for i in range(len(text)):
        print(text[i][0], text[i][1], text[i][3])