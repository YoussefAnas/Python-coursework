MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.', ' ': '/'}
def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        elif char == ' ':
            morse_code += '/'
        else:
            print(f"Invalid input: '{char}' is not a valid character.")
            return None
    return morse_code

def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        if code in MORSE_CODE_DICT.values():
            for key, value in MORSE_CODE_DICT.items():
                if code == value:
                    text += key
        elif code == '/':
            text += ' '
        else:
            print(f"Invalid input: '{code}' is not a valid Morse code.")
            return None
    return text

def main():
    user_input = input("Enter the text or Morse code you want to convert: ")
    if any(char.isalpha() for char in user_input):
        morse_result = text_to_morse(user_input)
        if morse_result is not None:
            print(f'Text to Morse Code: {morse_result}')
    else:
        text_result = morse_to_text(user_input)
        if text_result is not None:
            print(f'Morse Code to Text: {text_result}')

if __name__ == "__main__":
    main()

