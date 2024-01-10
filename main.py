import morse

#the user enters a text to be converted to morse
text_to_encode = input("Enter the text to convert to morse code:")

def morse_encode(text):
    #prepares the string for conversion, make it all lower case and remove non-allowed characters
    temp=text.lower()

    #encoded_text=morse.STARTING_SIGNAL
    encoded_text=''

    for char in temp:
        try:
            encoded_text+=morse.morse_dict[char]
        except KeyError as ke:
    # if the charcater is unknown a single space will be added
            encoded_text +=' '

    return encoded_text

print(f"Message converted to Morse code: {morse_encode(text_to_encode)}")
