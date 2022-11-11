import random


def generate_bingo_card():
    bvalues = [*range(1, 16, 1)]
    ivalues = [*range(16, 31, 1)]
    nvalues = [*range(31, 46, 1)]
    gvalues = [*range(46, 61, 1)]
    ovalues = [*range(61, 76, 1)]
    bingo_card = {'B': 0, 'I': 0, 'N': 0, 'G': 0, 'O': 0}
    for key, value in bingo_card.items():
        match key:
            case 'B':
                bingo_card[key] = random.sample(bvalues, 5)
            case 'I':
                bingo_card[key] = random.sample(ivalues, 5)
            case 'N':
                bingo_card[key] = random.sample(nvalues, 5)
            case 'G':
                bingo_card[key] = random.sample(gvalues, 5)
            case 'O':
                bingo_card[key] = random.sample(ovalues, 5)
    return bingo_card


def print_bingo_card(card: dict):
    print('════════════════════════║')
    print(' B  ║  I ║  N ║  G ║  O ║')
    print('════════════════════════║')
    for i in range(0, 5):
        for key, value in card.items():
            print(" {:02d}".format(card[key][i]), end=' ║')
        print('\n════════════════════════║')


if __name__ == "__main__":
    my_bingo_card = generate_bingo_card()
    print_bingo_card(my_bingo_card)
