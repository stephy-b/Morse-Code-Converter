from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

punctuation = ['.', ',', '?', '!', "'"]

morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-.--', '--..']

morse_numbers = ['.---', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']

morse_punctuation = ['.-.-.-', '--..--', '..--..', '-.-.--', '.----.']


def convert_to_morse(starting_text):
    '''Converts any String to Morse Code.  Regarding punctuation, only periods, commas, question marks, exclamation points, and apostrophes are converted if used.'''
    
    final_text = ""
    
    for char in starting_text:
        if char in alphabet:
            new_char = alphabet.index(char)
            morse_char = morse_alphabet[new_char]
            final_text += morse_char
            
        elif char in starting_text == ' ':
            morse_char = '.......'
            final_text += morse_char
            
        elif char in starting_text in punctuation:
            new_punc = punctuation.index(char)
            morse_punc = morse_punctuation[morse_punc]