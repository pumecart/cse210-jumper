from terminal_service import TerminalService
import random



class Word:
  def __init__(self):
    self._word_list = ["absolute",
                      "abstract",
                      "building",
                      "bulletin",
                      "business",
                      "calendar",
                      "campaign",
                      "victoria",
                      "violence",
                      "volatile",
                      "warranty",
                      "weakness",
                      "weighted",
                      "whatever",
                      "whenever",
                      "wherever",
                      "wildlife",
                      "wireless",
                      "withdraw",
                      "woodland",
                      "workshop",
                      "yourself"
                      ]
    self._letter_list = []
    self._TerminalService = TerminalService()
    
  def get_word(self):    
    # self.readFile = "words.txt"
    # # Word bank
    # with open("words.txt") as word_lists:
    #   for word in word_lists:
    #     word = word.strip()
    #     # print(word)
    #     self._word_list.append(word)
      # print(word_list)
    #Chooses words
    self._special_word = random.choice(self._word_list)
    print(self._special_word)

  # Set letter position
  def get_spaces(self, _special_word):

    for i in range(len(_special_word)):
      self._letter_list[i] = self._letter_list.append('_')

  def get_letter_guess(self):
    guess = self._TerminalService.read_letter("What is your guess: ")
    return guess

  def get_letter_position(self, _special_word, guess):
    
    # Set Blank Letters
    
      # i = special_word.index(guess)
    for i in range(len(_special_word)):
      if guess == _special_word[i]:
        # replace each index with the matching guess letter in special_word.
        # spaces[0:1] leaves "_" before the special_word[i]
        # spaces[i+1:] leaves "_" after the special_word[i]
        return i
      
  def set_letter_position(self, i, guess):
    self._letter_list[i] = guess
    
    print(self._letter_list)

  def incorrect_guess(self, _special_word, guess):
    value = 0

    for i in range(len(_special_word)):
      if guess != _special_word[i]:
        value += 1
        if value == 8:
          return 1
      else:
        return 0

  def guessed_word(self, _special_word):
    value = 0
    for i in range(len(_special_word)):
      if _special_word[i] == self._letter_list[i]:
        value += 1
        if value == 8:
          return True


        

      
    

#Mitchelle