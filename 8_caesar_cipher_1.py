print('''
                                        _       _               
   ___ __ _  ___  ___  __ _ _ __    ___(_)_ __ | |__   ___ _ __ 
  / __/ _` |/ _ \/ __|/ _` | '__|  / __| | '_ \| '_ \ / _ \ '__|
 | (_| (_| |  __/\__ \ (_| | |    | (__| | |_) | | | |  __/ |   
  \___\__,_|\___||___/\__,_|_|     \___|_| .__/|_| |_|\___|_|   
                                         |_|                    
''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while 3>2:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
#combination
    def caesar_cipher(new_text,shift_amount,new_direction):
        end_text = ""
        if(new_direction=="decode"):
            shift_amount*= -1        
        for letter in new_text:
            position = alphabet.index(letter)
            new_position = position+shift_amount
            end_text+=alphabet[new_position] 
        print(f"The {new_direction} text is {end_text}")
        
    caesar_cipher(new_text=text,shift_amount=shift,new_direction=direction)
# ###Encryption
#     def encrypt(plain_text,shift_amount):
#         cipher_text =""
#         for letter in plain_text:
        
#             position= alphabet.index(letter)
#             new_postion = position+shift_amount
#             new_letter =alphabet[new_postion]
#             cipher_text+= new_letter
#         print(f"The encode text is {cipher_text}")

# ###Decryption
#     def decrypt(cipher_text,shift_amount):
#         plain_text = ""
#         for letter in cipher_text:
#             position = alphabet.index(letter) 
#             new_position = position-shift_amount
#             plain_text+=alphabet[new_position]
#         print(f"The encode text is {plain_text}")
    # if(new_direction=="encode"): 
    #     encrypt(plain_text=text,shift_amount=shift )        
    # elif(new_direction == "decode"):
    #     decrypt(cipher_text=text,shift_amount=shift)
    # else:
    #     print("write correct word")     
    