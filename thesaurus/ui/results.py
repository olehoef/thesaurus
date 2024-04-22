from textual.widgets import Static, ListView, ListItem, Label
from textual.app import ComposeResult
from thesaurus.ui.association import Association

class Results(Static):
    def __init__(self, word):
        super().__init__()
        self.word = word
    
    def compose(self) -> ComposeResult:
        with ListView(id='results-container'):
            for i, sense in enumerate(self.word.senses):
                with ListItem(classes='associations-list'):
                    if sense.definition:
                        yield Label(f'[b]{str(i+1)}[/b] [i]' + sense.definition.replace("{it}", '').replace('{/it}','')+'[/i]')
                    if sense.syns != []:
                        yield Association(sense.syns,'Synonyms') 
                    if sense.rels != []:
                        yield Association(sense.rels,'Related') 
                    if sense.sims != []:
                        yield Association(sense.sims, 'Similar')