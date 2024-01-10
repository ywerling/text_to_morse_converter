import morse

#the user enters a text to be converted to morse
text_to_encode = input("Enter the text to convert to morse code:")


print(f"Message converted to Morse code: {morse.morse_encode(text_to_encode)}")
