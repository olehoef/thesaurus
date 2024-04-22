from textual.containers import Widget, Horizontal, Vertical
from textual.widgets import Label, Static
from textual.app import ComposeResult

class Association(Widget):

    def __init__(self, ass_group, ass_label):
        super().__init__()
        self.ass_group = ass_group
        self.ass_label = ass_label
    
    def compose(self) -> ComposeResult:
        with Horizontal(classes='association-container'):
            yield Label(f'[b]{self.ass_label}[/b]')
            yield Label('  ')
            with Vertical(classes='association-vert'):
                for i, group in enumerate(self.ass_group):
                    with Horizontal(classes='association-horizon'):
                        yield Label(str(i+1), classes='ass-num')
                        yield Label(' ')
                        if isinstance(group, list):
                            yield Static(', '.join(group), classes='ass-group')
                        elif isinstance(group, str):
                            yield Label(group)