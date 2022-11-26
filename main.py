from art import logo


morse_dictionary = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.---',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....', 
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '!': '-.-.--',
    ' ': '/',
}


def convert_to_morse(starting_text):
    '''Converts a string into Morse Code'''
    
    converted_message = []

    for char in starting_text:
        new_char = morse_dictionary.get(char)
        converted_message.append(new_char)
        
    print(''.join(converted_message))
    
    
print(logo)
power_on = True
while power_on:
    message = input('Type a message to convert into Morse Code:\n').lower()
    convert_to_morse(message)
    
    restart = input(f'Do you want to convert another message?  Type "yes" or "no".\n').lower()
    
    if restart == "no":
        print('Ok, goodbye.')
        power_on = False
    else:
        print("What?")