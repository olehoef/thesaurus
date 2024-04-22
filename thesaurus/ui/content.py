from textual.widgets import Static, Label
from textual.reactive import reactive
from textual.app import ComposeResult

from thesaurus.ui import Title, Results

class Content(Static):
    displayedWord = reactive(None, recompose=True)

    def __init__(self, mountWord, data_source):
        super().__init__()
        self.set_reactive(Content.displayedWord, mountWord)
        self.data_source = data_source

    def compose(self) -> ComposeResult:
        yield Title(self.displayedWord)
        yield Results(self.displayedWord) 
        yield Label(f'© Data from {self.data_source}', id='data-source')