from converter import convert_text

def end_program():
    global converter_is_on
    convert_more = input('Do you want to convert another word? Type "y" to continue\n').lower()
    if convert_more == "n":
        converter_is_on = False
        print("Thank you for using Text2Morse! See you soon!")
    elif convert_more == "y":
        pass
    else:
        print("invalid input - try again")
        end_program()

print('''
 _____         _     ____    __  __                     
|_   _|____  _| |_  |___ \\  |  \\/  | ___  _ __ ___  ___ 
  | |/ _ \\ \\/ / __|   __) | | |\\/| |/ _ \\| '__/ __|/ _ |
  | |  __/>  <| |_   / __/  | |  | | (_) | |  \\__ \\  __/
  |_|\\___/_/\\_\\\\___||_____| |_|  |_|\\___/|_|  |___/\\___|
  ''')
converter_is_on = True
while converter_is_on:
    print("Welcome to the Text2Morse Converter!")
    selected_word = input("Please type a word to convert:\n")
    convert_text(selected_word)
    end_program()





