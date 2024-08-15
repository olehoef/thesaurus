import click
import shutil
from thesaurus import datamodel

def render(word: datamodel.Word):
    

    click.clear()
    # Heading
    click.echo('\n')
    click.secho(f'{word.name.capitalize()}', bold=True, nl=False)
    click.secho(f'  {word.type}', color='grey', italic=True) if word.type else click.secho('', nl=True)
    click.echo('-'*80)
    click.echo('\n')
    
    # Content
    for i, sense in enumerate(word.senses):

        # Definition
        click.secho(f'{i+1} ', bold=True, nl=False)
        click.secho(sense.definition.replace('{it}', '').replace('{/it}',''), italic=True)
        

        # Synonyms
        if sense.syns != []:
            if type(sense.syns[0]) == str:
                _render_simple_syns(sense.syns, 'Synonymer')
            else:
                _render_association(sense.syns, 'Synonyms')

        # Related words
        if sense.rels != []:
            _render_association(sense.rels, 'Related')

        # Similar words
        if sense.sims != []:
            _render_association(sense.sims, 'Similar')
        
        # Spacer
        click.echo('\n')

    if word.examples:
        click.secho('Exempel  ', bold=True, nl=False)
        click.secho(word.examples.replace('&quot;', '"'))
    if word.idioms:
        click.secho('Uttryck  ', bold=True, nl=False)
        click.secho(word.idioms.replace('&quot;', '"'))


def _render_association(association_list, display_name):
    # Get the width of the terminal
    terminal_width = shutil.get_terminal_size().columns

    click.secho(display_name, bold=True, nl=False)
    click.echo(' ', nl=False)
    for i, syn_col in enumerate(association_list):
        # align subsequent rows
        if i > 0:
            click.echo(' ' * (len(display_name) + 1), nl=False)

        # print list
        line = ', '.join(syn_col)
        line_length = len(display_name) + len(line) + 1

        line_break= '\n' 
        indent = ' '*(len(display_name)+2)

        if line_length > terminal_width:
            wrapped_line = line
            break_line_index = -len(display_name)-1
            while line_length > terminal_width:
                # wrap line with full words
                break_line_index = find_pattern_backwards(wrapped_line, ',', break_line_index+terminal_width)
                wrapped_line = replace_at_index(wrapped_line, break_line_index, ','+line_break+indent)
                
                line_length = len(line[break_line_index:]) + len(indent)
                
            click.secho(wrapped_line, bold=False)
        else:
            wrapped_line = line
            click.echo(wrapped_line)

def find_pattern_backwards(string, pattern, start_index):
    index = string.rfind(pattern, 0, start_index)
    return index

def replace_at_index(string, index, new_char):
    string_list = list(string)
    string_list[index] = new_char
    new_string = ''.join(string_list)
    return new_string

def _render_simple_syns(synList, display_name):
    click.secho(display_name, bold=True, nl=False)
    for i, syn in enumerate(synList):
        click.echo('  ', nl=False)
        if i != 0:
            click.echo(' '*len(display_name), nl=False)
        click.echo(syn)