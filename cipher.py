import argparse
import math
'''
   Description: Cipher.py is a command line based tool that allows a user to pick between five different classic 
   ciphers: Caesar Cipher, Simple Substitution Cipher, Vignere Cipher, Transposition Cipher, and the Rail Fence 
   Cipher. The function arg_parser interprets all of the command line options given by the user and calls the necessary
   functions. 
'''

'''
   Description: A rail fence cipher broken into multiple functions to help make the calculations a little easier to 
   read. Essentially, a rail cipher takes plain text and writes it downwards and 
   diagonally on "rails" of an imaginary fence until the bottom of the fence is reached,
   in which case it starts to move up. The user can enter the number of rails needed. 
   Argument(s): mode - this can either be "encrypt" or "decrypt" depending on what operation the user wants to perform.
                message - the plaintext message to be encrypted or decrypted.
                num_rails - the amount of "rails" in the cipher.
            
   Return value: The message originally given to the function either encrypted or decrypted. 
'''


def rail_fence_encrypt(message, num_rails):
    return ''.join(fence(message, num_rails))


def rail_fence_decrypt(message, num_rails):
    rng = range(len(message))
    pos = fence(rng, num_rails)
    return ''.join(message[pos.index(n)] for n in rng)


''' 
   The calculations for actually determining the "rail"
'''


def fence(message, num_rails):
    fence = [[None] * len(message) for n in range(num_rails)]
    rails = list(range(num_rails - 1)) + list(range(num_rails - 1, 0, -1))
    for n, x in enumerate(message):
        fence[rails[n % len(rails)]][n] = x

    return [c for rail in fence for c in rail if c is not None]


'''
   The function below is the first portion of the Rail Fence Cipher; this function decides whether the 
   message needs to be encrypted or decrypted and calculates the rail based on that.
'''


def rail_fence_cipher(mode, message, num_rails):
    new_message = ""
    if(mode == "encrypt"):
        new_message = rail_fence_encrypt(message, num_rails)
    elif(mode == "decrypt"):
        new_message = rail_fence_decrypt(message, num_rails)

    return new_message


'''
    Description: A standard transposition cipher that uses a key passed by the user. A transposition cipher takes 
    the plaintext and systematically rearranges them into another pattern (in this case, using a key specified by 
    the user). See the README.md for more information on the usage. 
    Argument(s): mode - this can either be "encrypt" or "decrypt" depending on what operation the user wants to perform.
                 message - the message to be encrypted or decrypted.
                 key - the pattern to rearrange the plaintext with (or decrypt the ciphertext with) 
    Return value: The message after it has been encrypted or decrypted.
'''


def transposition_cipher(mode, message, key):
    print("I am a transposition cipher!")
    new_message = ""
    # Each string in the ciphertext represents a column in the grid
    if(mode == "encrypt"):
        ciphertext = [''] * key

        # looping through every column in the ciphertext
        for col in range(key):
            pointer = col

            while pointer < len(message):
                ciphertext[col] += message[pointer]
                pointer += key  # move pointer

        # Convert the ciphertext list into a string and then return it
        return ''.join(ciphertext)
    elif(mode == "decrypt"):
        '''
        The decrypt function emulates columns and rows 
        of the grid used by the plaintext by using a list 
        of strings.
        '''

        # num of columns in the transposition grid
        num_of_columns = math.ceil(len(message) / key)
        # num of rows in the grid
        num_of_rows = key
        # num of shaded boxes in the last column of the grid
        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(message)

        plaintext = [''] * num_of_columns

        # the col and row vars point to where in the grid the next
        # character in the encrypted message will go
        col = 0
        row = 0

        for letter in message:
            plaintext[col] += letter
            col += 1  # points at next column

            '''
            When there are no more columns or a shaded box is reached,
            we'll return back to the first column and the next row
            '''
            if(col == num_of_columns) or (col == num_of_columns - 1 and row >= num_of_rows - num_of_shaded_boxes):
                col = 0
                row += 1
        return ''.join(plaintext)


'''
    Description: A simple substitution cipher that simply matches up with the opposite end of the alphabet
    (ex: a maps to z, b maps to y, c maps to x, and etc. For the sake of simplicity, the alphabet mapping
    has been explicitly written, but a more dynamic and automated solution could use ASCII values and a Dictionary
    data structure to map these key and value pairs.
    Argument(s): mode - this can either be "encrypt" or "decrypt" depending on what operation the user wants to perform.
                 message - the message to be encrypted or decrypted.
    Return value: the encrypted or decrypted message after the cipher analyzes it.
'''


def simple_substitution_cipher(mode, message):
    new_message = ""
    alphabet = {
        "a": "z",
        "b": "y",
        "c": "x",
        "d": "w",
        "e": "v",
        "f": "u",
        "g": "t",
        "h": "s",
        "i": "r",
        "j": "q",
        "k": "p",
        "l": "o",
        "m": "n",
        "n": "m",
        "o": "l",
        "p": "k",
        "q": "j",
        "r": "i",
        "s": "h",
        "t": "g",
        "u": "f",
        "v": "e",
        "w": "d",
        "x": "c",
        "y": "b",
        "z": "a"
    }

    decryption_alphabet = {
        "z": "a",
        "y": "b",
        "x": "c",
        "w": "d",
        "v": "e",
        "u": "f",
        "t": "g",
        "s": "h",
        "r": "i",
        "q": "j",
        "p": "k",
        "o": "l",
        "n": "m",
        "m": "n",
        "l": "o",
        "k": "p",
        "j": "q",
        "i": "r",
        "h": "s",
        "g": "t",
        "f": "u",
        "e": "v",
        "d": "w",
        "c": "x",
        "b": "y",
        "a": "z"
    }

    message = message.lower()

    if mode == "encrypt":
        print("Encryption was chosen!")
        message = message.replace(" ", "")
        for letter in message:
            if letter not in alphabet:
                if letter != '\n':
                    new_message = new_message + letter
            else:
                new_message = new_message + alphabet[letter]

    elif mode == "decrypt":
        print("Decryption was chosen!")
        for letter in message:
            new_message = new_message + decryption_alphabet[letter]

    return new_message


'''
    Description: A Vigenere cipher that accepts a key passed by the user. The variable LETTERS is used to help
    help find the correct letter based on the key given by the user.
    Argument(s): mode - this can either be "encrypt" or "decrypt" depending on what operation the user wants to perform.
                 message - the message to be encrypted or decrypted.
                 key - The key to use for the encryption and decryption; this needs to be implemented still. 
    Return value: the encrypted or decrypted message after the cipher analyzes it.
'''


def vigenere_cipher(mode, message, key):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    my_key = "ASIMOV"
    translation = ""
    key_index = 0
    key = key.upper()

    for letter in message:
        num = LETTERS.find(letter.upper())  # find each char from the alphabet
        if num != -1:  # -1 indicates that it wasn't found in letters
            if mode == "encrypt":
                num += LETTERS.find(key[key_index])  # Add index for encryption
            elif mode == "decrypt":
                num -= LETTERS.find(key[key_index])  # Subtract index for decryption

            num %= len(LETTERS)  # Handle the possiblity of a wrap around

            # Add the new message to the end of the translation
            if letter.isupper():
                translation += LETTERS[num]
            elif letter.islower():
                translation += LETTERS[num].lower()

            key_index += 1  # shifts to the next letter in the key

            if key_index == len(my_key):
                key_index = 0  # repeats the key if it's finished
        else:
            translation += letter
        # If the symbol isn't found in the string LETTERS, then
        # it'll be appended as its default value
    return translation


''' 
    Description: An implementation of Caesar cipher that uses dictionaries to find the correct letter translations.
    Letters not in the alphabet are printed as they are. A caesar cipher simply "shifts" letters of the alphabet over
    by x number of spaces, in this case, 3 spaces. This means that the character a in plaintext becomes d in ciphertext
    and the character b becomes e in ciphertext. 
    Argument(s): mode - this can either be "encrypt" or "decrypt" depending on what operation the user wants to perform.
                 message - the message to be encrypted or decrypted.
    Return value: The decrypted or encrypted message after being analyzed by the function. 
'''


def caesar_cipher(mode, message):
    new_message = ""
    message = message.lower()
    print("I'm a Caesar Cipher!")
    alphabet = {
                "a": "d",
                "b": "e",
                "c": "f",
                "d": "g",
                "e": "h",
                "f": "i",
                "g": "j",
                "h": "k",
                "i": "l",
                "j": "m",
                "k": "n",
                "l": "o",
                "m": "p",
                "n": "q",
                "o": "r",
                "p": "s",
                "q": "t",
                "r": "u",
                "s": "v",
                "t": "w",
                "u": "x",
                "v": "y",
                "w": "z",
                "x": "a",
                "y": "b",
                "z": "c"
                }

    decryption_alphabet = {
                "d": "a",
                "e": "b",
                "f": "c",
                "g": "d",
                "h": "e",
                "i": "f",
                "j": "g",
                "k": "h",
                "l": "i",
                "m": "j",
                "n": "k",
                "o": "l",
                "p": "m",
                "q": "n",
                "r": "o",
                "s": "p",
                "t": "q",
                "u": "r",
                "v": "s",
                "w": "t",
                "x": "u",
                "y": "v",
                "z": "w",
                "a": "x",
                "b": "y",
                "c": "z"
                }

    if mode == "encrypt":
        print("Encryption was chosen!")
        for letter in message:
            if letter not in alphabet: #adds the letter if it's not in the alphabet as it is
                new_message = new_message + letter
            else: #appends the correct letter to the new_message
                new_message = new_message + alphabet[letter]
                print("Caesar did this: " + new_message)

    elif mode == "decrypt":
        print("Decryption was chosen!")
        for letter in message:
            if letter not in alphabet:
                new_message = new_message + letter
            else:
                new_message = new_message + decryption_alphabet[letter]

    return new_message


''' 
    Description: File writer for the new messages 
    Argument(s): write_content - the content to be written to the file.
                 file_name - the name of the file to be written to.
    Return value: None
'''


def file_writer(write_content, file_name):
    print("I'm a file writer!")
    f = open(file_name, "w")
    f.write(write_content)


'''
    Description: File reader for the files passed in the command line.
    Argument(s): file_name - the name of the file to be open and read from.
    Return value: The content read from the file. 
'''


def file_reader(file_name):
    print("I'm a file reader!")
    file_content = ""
    f = open(file_name, "r")
    while True:  # Traverses file until all the lines have been read
        c = f.readline()
        if not c:
            print("End of file")
            break
        file_content = file_content + c

    return file_content


'''
    Description: The function below parses the arguments passed in by the user; there are many different commands that
    the user can enter to to utilize different ciphers; please see the readme for more details.
    Argument(s): None
    Return value: None
'''


def arg_parser():
    new_msg = ""
    msg = ""
    isFile = False
    print("test")
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="Choose whether to encrypt or decrypt")
    parser.add_argument("-c", "--caesar", default="check_for_empty_string", help="use the Caesar cipher algorithm",
                        action="store_true")
    parser.add_argument("-ss", "--sub", default="check_for_empty_string", help="use the simple substitution "
                        "algorithm", action="store_true")
    parser.add_argument("-pa", "--poly_alpha", default="check_for_empty_string", help="use the Vigenere cipher"
                        "algorithm", action="store_true")
    parser.add_argument("-tr", "--trans", default="check_for_empty_string", help="use the transposition cipher"
                        "algorithm", action="store_true")
    parser.add_argument("-rfc", "--rail", default="check_for_empty_string", help="use the rail fence cipher"
                        "algorithm", action="store_true")
    parser.add_argument("-fow", help="Choose the file to be encrypted or decrypted or enter a message to be encrypted")
    parser.add_argument("-output", help="Name the file that you want the output to be written to")
    parser.add_argument("-key", default = 'check_for_empty_string', help="specify the key to use on the "
                        "algorithm (only works for certain functions where "
                        "a key is relevant")

    args = parser.parse_args()

    '''Checks for if the user is entering a word or a text file name'''
    if ".txt" in args.fow:
        msg = file_reader(args.fow)

    '''The rest of this function figures what cipher was chosen and the values of the other cmd args'''
    if args.caesar == 'check_for_empty_string':
        pass
    elif args.caesar:
        print("Caesar Cipher was chosen")
        new_msg = caesar_cipher(args.action, msg)
        print("Your new message is: " + new_msg)

    if args.sub == 'check_for_empty_string':
        pass
    elif args.sub:
        if args.key != 'check_for_empty_string':
            print("This particular cipher does not accept a key")
            return

        print("Simple Substitution was chosen")
        new_msg = simple_substitution_cipher(args.action, msg)

    if args.poly_alpha == 'check_for_empty_string':
        pass
    elif args.poly_alpha:
        print("Poly-Alphabetic Cipher was chosen")
        if args.key != "check_for_empty_string":
            new_msg = vigenere_cipher(args.action, msg, args.key)
        else:
            print("You need a key for this cipher; please enter a key")
            return

    if args.trans == 'check_for_empty_string':
        pass
    elif args.trans:
        print("Transposition cipher was chosen")
        if args.key != 'check_for_empty_string':
            try:
                y = int(args.key)
                new_msg = transposition_cipher(args.action, msg, y)
            except:
                print("Please enter an integer as a key for this cipher.")
                return

        else:
            print("Please enter an integer as a key for this cipher.")
            return

    if args.rail == 'check_for_empty_string':
        pass
    elif args.rail:
        print("Rail Cipher was chosen")
        if args.key != 'check_for_empty_string':
            try:
                y = int(args.key)
                new_msg = rail_fence_cipher(args.action, msg, y)
            except:
                print("Please enter an integer as a key for this cipher.")

        else:
            print("Please enter an integer as a key for this cipher.")
            return

    '''removes whitespace from the new message and writes it to the necessary file'''

    if args.trans =='check_for_empty_string':
        new_msg = new_msg.replace(" ", "")

    print("Your new message is: \n" + new_msg)
    file_writer(new_msg, args.output)


def main():
    arg_parser()


main()
