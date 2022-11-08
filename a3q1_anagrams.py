def are_anagrams(word1: str, word2: str) -> bool:
    dictionary1 = {}
    dictionary2 = {}
    word1 = word1.lower()
    word2 = word2.lower()
    for letter in word1:
        if letter in dictionary1:
            dictionary1[letter] += 1
        else:
            dictionary1[letter] = 1
    for letter in word2:
        if letter in dictionary2:
            dictionary2[letter] += 1
        else:
            dictionary2[letter] = 1
    # print(dictionary1,dictionary2)
    if dictionary1 == dictionary2:
        return True
    else:
        return False


if __name__ == '__main__':
    print("~~~Enter two words to check if they are anagrams~~~")
    user_word1 = input('Enter Word 1: ')
    user_word2 = input('Enter Word 2: ')
    anagram_check = are_anagrams(user_word1, user_word2)
    if not anagram_check:
        print(f'{user_word1}, and {user_word2} are not anagrams!')
    else:
        print(f'{user_word1}, and {user_word2} are anagrams!')

