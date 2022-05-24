from terminal_service import TerminalService
from word_choice import Word
from jumper_image import JumperImage

class Director:
    def __init__(self):
        self._isPlaying = True
        self._TerminalService = TerminalService()
        self._Word = Word()
        self._JumperImage = JumperImage()
    

    def start_game(self):
        while self._isPlaying:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
    
    def _get_inputs(self):
        print()

    def _do_updates(self):
        print()

    def _do_outputs(self):
        print()