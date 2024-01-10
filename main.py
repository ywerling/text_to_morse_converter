import morse

#the user enters a text to be converted to morse
text_to_encode = input("Enter the text to convert to morse code:")

#prepares the string for conversion and remove non allowed characters
temp=text_to_encode.lower()

#encoded_text=morse.STARTING_SIGNAL
encoded_text=''

for char in temp:
    try:
        encoded_text+=morse.morse_dict[char]
    except KeyError as ke:
# if the charcater is unknown a single space will be added
#        print(ke)
        encoded_text +=' '

print(f"Message converted to Morse code: {encoded_text}")
