import click, sys, inquirer
from thesaurus import datamodel, renderer, input_handlers, rest
from thesaurus.ui.app import UIApp





@click.command()
@click.option('--english', '-en', 'lang', flag_value='en', default=True)
@click.option('--svenksa', '-sv', 'lang', flag_value='sv')
@click.option('--deutsch', '-de', 'lang', flag_value='de')
@click.option('--user-interface/--plain-text', '-ui/-pt', 'ui', default=True)
@click.argument('search_phrase')
def cli(search_phrase,lang,ui):
    thesaurus = datamodel.Thesaurus()

    # Render thesaurus output
    if ui:
        match lang:
            case 'en':
                input_handlers.handle_en_ui(thesaurus, search_phrase)
            case 'sv':
                input_handlers.handle_sv_ui(thesaurus, search_phrase)
            case 'de':
                click.secho('DE not configured yet!', fg='red')
                sys.exit()
        
        UIApp(word=thesaurus.words[0], lang=lang, th=thesaurus).run()
    else:
        # Handle user input
        match lang:
            case 'sv':
                chosen_word = input_handlers.handle_sv_input(thesaurus, search_phrase)
            case 'de':
                click.secho('DE not configured yet!', fg='red')
                sys.exit()
            case 'en':
                thesaurus, chosen_word = input_handlers.handle_en_input(thesaurus, search_phrase)

        renderer.render(chosen_word)
