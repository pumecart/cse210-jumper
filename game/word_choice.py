import random


class Word:
  def __init__(self):
    self._word_list = []
    self._index = -2
    
  def get_word(self):    
    self.readFile = "words.txt"
    # Word bank
    with open("words.txt") as word_lists:
      for word in word_lists:
        word = word.strip()
        # print(word)
        self._word_list.append(word)
      # print(word_list)
    #Chooses words
    self._special_word = random.choice(self._word_list)
    print(self._special_word)

  # Set letter position
  def get_spaces(self, _special_word):
    self.spaces = "_"*len(_special_word)
    print(self.spaces)

  def get_letter_position(self, _special_word, _index):
    while _index != -1:
    # Set Blank Letters
      guess = input("What is your guess: ")
      # i = special_word.index(guess)
      for i in range(len(_special_word)):
        if guess == _special_word[i]:
          # replace each index with the matching guess letter in special_word.
          # spaces[0:1] leaves "_" before the special_word[i]
          # spaces[i+1:] leaves "_" after the special_word[i]
          self.spaces = self.spaces[0:i] + guess + self.spaces[i+1:]
      # print(display)
          print(self.spaces)
        

      
    

#Mitchelle