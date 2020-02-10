# Classic-Ciphers
Version: Python 3.4

Description: Cipher.py is a commamd-line tool that allows a user to pick between 5 different classic ciphers to either encrypt or decrypt messages in a file and write them to a different file.

## Features:
  ### Five Classic Ciphers for both encryption and decryption: 
     1) Caesar Cipher
     2) Simple Substitution Cipher
     3) Vigenere Cipher
     4) Transposition Cipher
     5) Rail Fence Cipher
  ### File reader and writer: 
  Cipher.py can read txt files passed through the command prompt and can write them to another specificed file
  ### Command line tool:
  Users can use the command line tool to type in file names to both read and write, choose a cipher, decide whether they    want to encrypt or decrypt, and even pass keys for the classic ciphers that support it. 
  ### Custom key compatibility
  Users can type a key into the command line tool to use it for the encrypting or decrypting certain ciphers that support
  the functionality. Caesar Cipher and Substitution Cipher do NOT support this functionality.
      
## How to Use the Command Line Tool: 
  There will be an extensive list of commands for each different component of the command line arguments listed below 
  
  #### Here's an example of a command: 
    python3 cipher.py encrypt -c -fow test.txt -output testoutput.txt
  
  The general format is as follows: python3 cipher.py action -type_of_cipher -fow file_name -output write_to_this_file
  
  In the above example, the action is "encrypt". The -type_of_cipher is "-c", which stands for Caesar. "-fow" refers to the
  file or word to be translated; in this case, the file name is test.txt. The "-output" refers to the output file to be written
  to. In this case, the output file is called testoutput.txt
  
  ### An Example of one command for each cipher for both encryption and decryption
    Caesar Cipher command examples
    1) python3 cipher.py encrypt -c -fow ctest.txt -output testoutput.txt 
    2) python3 cipher.py decrypt -c -fow testoutput.txt -output ctest.txt 
    
    Simple Substitution Cipher command examples
    3) python3 cipher.py encrypt -ss -fow sstest.txt -output testoutput.txt 
    4) python3 cipher.py decrypt -ss -fow testoutput.txt -output sstest.txt 
    
    Vigenere Cipher command examples
    5) python3 cipher.py encrypt -pa -fow vtest.txt -output testoutput.txt -key ASIMOV 
    6) python3 cipher.py decrypt -pa -fow testoutput.txt -output vtest.txt -key ASIMOV 
    
    Transposition Cipher command examples
    7) python3 cipher.py encrypt -tr -fow trtest.txt -output testoutput.txt -key 8 
    8) python3 cipher.py decrypt -tr -fow testoutput.txt -output trtest.txt -key 8 
    
    Rail Fence Cipher command example
    9) python3 cipher.py encrypt -rfc -fow rfctest.txt -output testoutput.txt -key 3 
    10) python3 cipher.py decrypt -rfc -fow testoutput.txt -output rfctest.txt -key 3 
  
  ### List of commands for components of the command line tool
    1) action: 
      encrypt - lets the program know that you want to encrypt a file 
      decrypt - lets the program know that you want to decrypt a file 
    2) -type_of_cipher 
      -c -> means that you want to use the Caesar cipher 
      -ss -> means that you want to use the simple substitution cipher 
      -pa -> means that you want to use the Vigenere cipher (pa means poly-alphabetical) 
      -tr -> means that you want to use the transposition cipher 
      -tfc -> means that you want to use the rail fence cipher 
    3) -fow file_name 
        - Simply type "-fow " followed by the name of the file you want to read (make sure it's a txt file with '.txt' at the 
      end of it) 
     4) -output write_to_this_file 
        - Simply type "-output " followed by the name of the file you want to write the translation to.
     5) -key number_or_string 
        -Simply type "-key " followd by a string of letters or a number depending on the type of cipher; transposition cipher
        and rail fence cipher both take numbers as their key.
 
