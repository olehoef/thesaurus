from textual.app import ComposeResult
from textual.widgets import Static, Button, ListView, ListItem
from textual.message import Message


class Sidebar(Static):
    def __init__(self, th):
        super().__init__()
        self.th = th

    def compose(self) -> ComposeResult:
        with ListView():
            for word in self.th.words:
                yield ListItem(SideBtn(word), classes='sidebar-item')


class SideBtn(Static):

    class Selected(Message):
        """Color selected message."""

        def __init__(self, selectedWord) -> None:
            self.selectedWord = selectedWord
            super().__init__()

    def __init__(self, word) -> None:
        self.word = word
        self.type_string = f'({self.word.type})' if self.word.type else ''
        super().__init__()


    def on_click(self) -> None:
        # The post_message method sends an event to be handled in the DOM
        self.post_message(self.Selected(self.word))

    def render(self) -> str:
        return f'{self.word.name} {self.type_string}'
