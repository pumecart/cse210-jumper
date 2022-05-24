# Print in the terminal with inputs
#Logan McCauley
#Pume
class TerminalService:

    def read_text(self, prompt):
        return input(prompt)

    def read_letter(self, prompt):
        return input(prompt)

    def write_text(self, text):
        print(text)