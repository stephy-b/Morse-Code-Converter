from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

punctuation = ['.', ',', '?', '!']

morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']

morse_numbers = ['.---', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']

morse_punctuation = ['.-.-.-', '--..--', '..--..', '-.-.--']


def convert_to_morse(starting_text):
    '''Converts any String into Morse Code.  Regarding punctuation, only periods, commas, question marks and exclamation points are converted if used.'''
    
    final_text = ""
    
    for char in starting_text:
        if char in alphabet:
            new_char = alphabet.index(char)
            morse_char = morse_alphabet[new_char]
            final_text += morse_char + ' '
            
        elif char in numbers:
            new_num = numbers.index(char)
            morse_num = morse_numbers[new_num]
            final_text += morse_num + ' '
                        
        elif char in punctuation:
            new_punc = punctuation.index(char)
            morse_punc = morse_punctuation[new_punc]
            final_text += morse_punc + ' '
            
        elif char in starting_text == ' ':
            morse_char = '.......'
            final_text += morse_char + ' '
            
        else:
            final_text += char
            
    return final_text
            

print(logo)

game_on = True
while game_on:
    message_to_convert = input('Type a message to convert into Morse Code:\n').lower()
    
    converted_message = convert_to_morse(message_to_convert)
    print(converted_message)
    
    restart = input(f'Do you want to convert another message?  Type "yes" or "no".\n').lower()
    
    if restart == "no":
        print('Ok, goodbye.')
        game_on = False
    else:
        print("What?")
