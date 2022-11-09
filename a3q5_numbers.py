def write_out_number(number: int) -> str:
    stringnumber = str(number)
    length = len(stringnumber)
    words = [{'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven'
                 , '8': 'eight', '9': 'nine'}, {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen'
                 , '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen'
                 , '19': 'nineteen'}, {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty'
                 , '7': 'seventy', '8': 'eighty', '9': 'ninety', }]

    if number < 10:  # Single digit
        return words[0][stringnumber]
    elif length == 2 and number < 20:  # Between 10 and 19
        return words[1][stringnumber]
    elif length == 2 and number >= 20:  # Between 20 and 99
        written = words[2][stringnumber[0]]
        written += ' '
        written += words[0][stringnumber[1]]
        return written
    elif length == 3 and stringnumber[1] != '1':  # Between 100 and 999 where the second number is not one
        written = words[0][stringnumber[0]]
        written += ' '
        written += 'hundred'
        written += ' '
        written += words[2][stringnumber[1]]
        written += ' '
        written += words[0][stringnumber[2]]
        return written
    else:  # Between 100 and 999 where the second number is one
        written = words[0][stringnumber[0]]
        written += ' '
        written += 'hundred'
        written += ' '
        written += words[1][stringnumber[1:]]
        return written


if __name__ == "__main__":
    print("~~~Enter a number to recieve its written form~~~")
    user_num = int(input('Enter a word: '))
    print(f'{user_num} written out is: {write_out_number(user_num)}')
