import nltk
import re
from corpus_loader import word_list, name_list # Import the word_list and name_list from corpus_loader.py

def encrypt(plain, shift): # Define the encrypt function
  encrypted_text = ""
  number_of_characters = 26 # The number of characters in the English alphabet

  for char in plain: # Loop through each character in the plain text
    if char.isalpha(): 
      if char.islower(): 
        base_character = "a" 
      else:
        base_character = "A" # Otherwise, set the base character to "A"
      base_code = ord(base_character) # Get the Unicode code of the base character
      current_code = ord(char)
      current_position = current_code - base_code
      shifted_position = (current_position + shift) % number_of_characters # Shift the position by the shift amount
      shifted_code = base_code + shifted_position # Get the Unicode code of the shifted character
      encrypted_text += chr(shifted_code)
    else:
      encrypted_text += char

  return encrypted_text
  
# print(ord(" "))

def decrypt(encrypted_text, shift):
  return encrypt(encrypted_text, -shift)

def crack(encrypted_text):
    word_count = 0
    cracked_text = ""
    for i in range(26):  # Try all 26 possible shifts
        decrypted_subject = decrypt(encrypted_text, i)
        words = decrypted_subject.split()  # Split the decrypted text into words
        for word in words:
            if word.lower() in word_list or word in name_list:
                word_count += 1
                cracked_text += word + " "  # Add the word to the cracked text

    if word_count == 0:
        return None # No words were found
    else:
        return cracked_text.strip()
  
    

if __name__ == "__main__":
    sample = "AAAA"
    result = encrypt(sample, 1)
    print(result)  # Print the result