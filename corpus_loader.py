import ssl
import nltk
from nltk.corpus import words, names # Import the words and names corpus from nltk


try:
  _create_unverified_https_context = ssl._create_unverified_context # Create an unverified context
except AttributeError:
  pass
else:
  ssl._create_default_https_context = _create_unverified_https_context # Set the default context to the unverified context

nltk.download("words", quiet=True) 
nltk.download("names", quiet=True)

word_list = words.words()
name_list = names.words()