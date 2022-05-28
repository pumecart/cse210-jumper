<<<<<<< HEAD
from terminal_service import TerminalService
from word_choice import Word
from jumper_image import Jumper_image
=======
from game.terminal_service import TerminalService
from game.word_choice import Word
from game.jumper_image import Jumper_image
>>>>>>> 79d8c37b91b3d465eb30133296e0f761a4f26653

class Director:
    def __init__(self):
        self._isPlaying = True
        self._TerminalService = TerminalService()
        self._Word = Word()
        self._JumperImage = Jumper_image()
        self._Goal = Word.get_word(self)
        Word.get_spaces(self._Goal)
        Jumper_image.print_jumper(0)
        self._guess = ""
        self._letter_position = 0
        self._incorrect = 0
        self._win = False
    

    def start_game(self):
        while self._isPlaying:
            self._get_inputs()
            self._do_updates()
<<<<<<< HEAD
            break
    #         self._do_outputs()
    
    def _get_inputs(self):
        # self._guess = self._Word.get_letter_guess()
        self.guess =  self._TerminalService.read_letter(input("What is your guess: "))

    def _do_updates(self):
        self._Goal = self._Word.get_letter_position(self._Word.get_word("words.txt"), self._index)
        # self._Word.get_spaces(self._Goal)
        # self._letter_position = self._Word.get_letter_position(self._index, self._Word.get_word("words.txt"))
       
        
    #     self._incorrect += self._Word.incorrect_guess(self._Goal, self._guess)
    #     if self._incorrect == 5:
    #         self._isPlaying = False
    #     self._win = self._Word.guessed_word(self._Goal)
    #     if self._win == True:
    #         self._isPlaying = False

    # def _do_outputs(self):
    #     self._Word.set_letter_position(self._letter_position, self._guess)
    #     self._JumperImage.print_jumper(self._incorrect)
=======
            self._do_outputs()
    
    def _get_inputs(self):
        self._guess = self._Word.get_letter_guess()

    def _do_updates(self):
        self._letter_position = self._Word.get_letter_position(self._Goal, self._guess)
       
        
        self._incorrect += self._Word.incorrect_guess(self._Goal, self._guess)
        if self._incorrect == 5:
            self._isPlaying = False
        self._win = self._Word.guessed_word(self._Goal)
        if self._win == True:
            self._isPlaying = False

    def _do_outputs(self):
        self._Word.set_letter_position(self._letter_position, self._guess)
        self._JumperImage.print_jumper(self._incorrect)
        if self._incorrect == 5:
            self._TerminalService.write_text("Sorry, you're parachute disappeared and the Jumper has died.  Thanks for killing him.")
        self._win = self._Word.guessed_word(self._Goal)
        if self._win == True:
            self._TerminalService.write_text(f"Congratulations!!! You guessed {self._Goal} correctly!!!  Thanks for keeping the Jumper alive!!!")
        
>>>>>>> 79d8c37b91b3d465eb30133296e0f761a4f26653
