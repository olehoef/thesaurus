from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import  Header,  Footer, Label
from textual.binding import Binding
from textual.reactive import reactive

from thesaurus.ui import Sidebar, SideBtn, Content



class UIApp(App):
    """Displays Thesaurus Output."""

    CSS_PATH = "dictionary.tcss"
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app")
    ]
    displayedWord = reactive(None, recompose=True)
    def __init__(self, word, lang, th):
        super().__init__()       
        self.word = word
        self.lang = lang
        self.th = th
        self.data_source = ''
        self.set_reactive(UIApp.displayedWord, word)
        match(lang):
            case 'en':
                self.data_source = 'Merriam-Webster'
            case 'sv':
                self.data_source = 'synonymord.se'

    

    def compose(self) -> ComposeResult:
        #yield Input(placeholder="Search for a word")
        yield Header()
        with Container(id='content'):
            with Horizontal(id='content-horizon'):
                yield Sidebar(self.th)
                yield Content(self.word, self.data_source)
        yield Footer()
    
    def on_side_btn_selected(self, message: SideBtn.Selected) -> None:
        self.query_one(Content).displayedWord = message.selectedWord


    def on_mount(self) -> None:
        """Called when app starts."""
        match(self.lang):
            case 'en':
                self.sub_title = 'English'
            case 'sv':
                self.sub_title = 'svenska'
        self.title = 'Thesaurus'


    

