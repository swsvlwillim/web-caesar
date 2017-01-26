def alphabet_position(letter):
    """returns the positon number of a letter"""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()
    for i in alphabet:
        return alphabet.index(letter)    
    
     
def rotate_character(char, rot):
   """ Returns character at rotated position """
   if not char.isalpha():
       return char

   alphabet = 'abcdefghijklmnopqrstuvwxyz'
   new_position = (alphabet_position(char) + rot) % 26
   for i in char:
       if char.isupper():
           return alphabet[new_position].upper()
       else:
           return alphabet[new_position].lower()

def encrypt(text, rot):
    """returns a str of text moved rot spaces over"""      
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
   
    for char in text:
        encrypted = encrypted+ rotate_character(char,rot)
    return encrypted 