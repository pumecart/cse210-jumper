from terminal_service import TerminalService
from word_choice import Word
from jumper_image import Jumper_image

class Director:
    def __init__(self):
        self._isPlaying = True
        self._TerminalService = TerminalService()
        self._Word = Word()
        self._JumperImage = Jumper_image()
        self._Goal = Word.get_word()
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
        