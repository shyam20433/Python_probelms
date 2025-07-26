MORSE_CODE_DICT = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',   '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',
    '0': '-----',  ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.',  ')': '-.--.-', ' ': '/'
}



def encode(text):
    return " ".join([MORSE_CODE_DICT.get(i.upper()) for i in text])

print(encode("shyam sundar"))



def decode(code):
    reverse={ value:key.lower() for key,value in MORSE_CODE_DICT.items() }
    return "".join([reverse.get(i) for i in code.split()])
print(decode(encode("shyam sundar")))


a=["shyam","sundar","cat"]
for i in a:
    print(encode(i))
