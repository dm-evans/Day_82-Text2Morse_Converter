from library import letters_dict


def convert_text(string):
    new_string = " ".join(letters_dict.get(letter) for letter in string.upper())
    print(new_string)



