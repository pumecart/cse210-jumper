import random

#Create a list of words to choose from for the user to guess
words = ["computer", "science", "programmer", "python", "developer", "geeks", "youtube", "mathematics" ]

#Randomly choose one of the listed words
word = random.choice(words)
#Show word
print(word)

# Create "n" underscores to represent character spaces
spaces = ["_"]*len(word)
#show spaces
print(spaces)

#Create a function
#1. Finall all of the letter positions from the users guess(some characters)
#2. If the letter exists in the word then replace the underscores n spaes with the correct letter(s) in that position 

def get_letter_position(guess, word, spaces):
  #Create and set index to be -2
  index = -2
  while index != -1:
    #Check if the character or quess is in word, if it is then remove the character from the word and add it to spaces
    if guess in word:
      index = word.find(guess)
      #Remove that letter from the word
      removed_character = "*"
      word = word[:index] + removed_character + word[index + 1:]
      spaces[index] = guess
    else:
      index = -1
  return(word, spaces)

#Creata  function to check if the user guessed all of the letters in the word (1 = Yes, -1=No)
def win_check():
  for i in range(0, len(spaces)):
    if spaces[i] == "_":
      return -1
  return 1

#Choose some number of turns for the user to guess the word
num_turns = len(word)
for i in range(0, num_turns):
  #Ask the user to guess a character
  guess = input("Guess a character: ")
  
  if guess in word:
    word, spaces =  get_letter_position(guess, word, spaces)
    print(spaces)
  else:
    print("Sorry that letter is not in the word.")
    #Check if the player guessed the word
  if win_check() == 1:
    print("Congratulations You Won!!")
    break
  print("You have" + " " + str(num_turns - i) + " turns left.")
  print()
      