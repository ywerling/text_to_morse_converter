#source: Wikipedia: https://en.wikipedia.org/wiki/Morse_code (status January 2024)


    # short mark, dot or dit (  ▄ ): '1'b
    # longer mark, dash or dah (  ▄▄▄ ): '111'b
    # intra-character gap (between the dits and dahs within a character): 0
    # short gap (between letters): '000'b
    # medium gap (between words): '0000000'b

STARTING_SIGNAL='▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ '

morse_dict = {
                'a': '▄ ▄▄▄ ',
                'b': '▄▄▄ ▄ ▄ ▄ ',
                'c': '▄▄▄ ▄ ▄▄▄ ▄ ',
                'd': '▄▄▄ ▄ ▄ ',
                'e': '▄ ',
                'f': '▄ ▄ ▄▄▄ ▄ ',
                'g': '▄▄▄ ▄▄▄ ▄ ',
                'h': '▄ ▄ ▄ ▄ ',
                'i': '▄ ▄ ',
                'j': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ',
                'k': '▄▄▄ ▄ ▄▄▄ ',
                'l': '▄ ▄▄▄ ▄ ▄ ',
                'm': '▄▄▄ ▄▄▄ ',
                'n': '▄▄▄ ▄ ',
                'o': '▄▄▄ ▄▄▄ ▄▄▄ ',
                'p': '▄ ▄▄▄ ▄▄▄ ▄ ',
                'q': '▄▄▄ ▄▄▄ ▄ ▄▄▄ ',
                'r': '▄ ▄▄▄ ▄ ',
                's': '▄ ▄ ▄ ',
                't': '▄▄▄ ',
                'u': '▄ ▄ ▄▄▄ ',
                'v': '▄ ▄ ▄ ▄▄▄ ',
                'w': '▄ ▄▄▄ ▄▄▄ ',
                'x': '▄▄▄ ▄ ▄ ▄▄▄ ',
                'y': '▄▄▄ ▄ ▄▄▄ ▄▄▄ ',
                'z': '▄▄▄ ▄▄▄ ▄ ▄ ',
                '0': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ',
                '1': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ',
                '2': '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄ ',
                '3': '▄ ▄ ▄ ▄▄▄ ▄▄▄ ',
                '4': '▄ ▄ ▄ ▄ ▄▄▄ ',
                '5': '▄ ▄ ▄ ▄ ▄ ',
                '6': '▄▄▄ ▄ ▄ ▄ ▄ ',
                '7': '▄▄▄ ▄▄▄ ▄ ▄ ▄ ',
                '8': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄ ',
                '9': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄ ',
                '.': '▄ ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ',
                ',': '▄▄▄ ▄▄▄ ▄ ▄ ▄▄▄ ▄▄▄ ',
                '?': '▄ ▄ ▄▄▄ ▄▄▄ ▄ ▄ ',
                '!': ' ▄▄▄ ▄ ▄▄▄ ▄ ▄▄▄ ▄▄▄ ',
}

def morse_encode(text):
    #prepares the string for conversion, make it all lower case and remove non-allowed characters
    temp=text.lower()

    #the encoded message can start either as blank or with the code of the starting signal
    #encoded_text=STARTING_SIGNAL
    encoded_text=''

    for char in temp:
        try:
            encoded_text+=morse_dict[char]
        except KeyError as ke:
    # if the charcater is unknown a single space will be added
            encoded_text +=' '

    return encoded_text


