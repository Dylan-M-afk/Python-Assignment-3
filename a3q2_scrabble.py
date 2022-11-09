def get_scrabble_score_for_word(word: str) -> int:
    score = 0
    word = word.lower()
    score_dictionary = {'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'd': 2, 'g': 2,
                        'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 8,
                        'x': 8, 'q': 10, 'z': 10, }
    for letter in word:
        if letter in score_dictionary:
            score += score_dictionary[letter]
    return score


if __name__ == '__main__':
    print("~~~Enter a word to check its Scrabble™ Score~~~")
    user_word = input('Enter a word: ')
    print(f'The Scrabble™ score for {user_word} is: {get_scrabble_score_for_word(user_word)}')
