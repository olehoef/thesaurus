from textual.widgets import Static, Label, Rule
from textual.app import ComposeResult

class Title(Static):
    def __init__(self, word):
        super().__init__()
        self.word = word
        self.type_string = f'[i]{self.word.type}[/i]' if self.word.type else ''


    def compose(self) -> ComposeResult:
        yield Label(f'[b]{self.word.name}[/b]  {self.type_string}', id='heading-label')
        yield Rule()