#Main game code
from word_choice import Word
word = Word()
word.get_word()
word.get_spaces(word._special_word)
word.get_letter_position(word._special_word, word._index)