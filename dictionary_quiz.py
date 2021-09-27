with open('data/vocabulary.txt', 'r') as f:       #open file
    for line in f:
        data = line.strip().split((': '))


        kor = input(f'{data[1]}: ')                #guessing Korean word in English
        eng = data[0]
        if kor == eng:
            print('맞았습니다\n')
        else:
            print(f'아쉽습니다. 정답은 {eng}입니다.\n')
