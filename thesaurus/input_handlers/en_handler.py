from thesaurus import datamodel, rest
import click, sys, inquirer


def handle_en_input(th:datamodel.Thesaurus, search_phrase:str) -> datamodel.Word:

    data = rest.request_thesaurus_en(search_phrase)


    if data == []:
        click.echo('\nNo word found. Please try again.')
        sys.exit()
    elif type(data[0]) == str:
        choices = [
            inquirer.List(
                'choice',
                message='No direct match. Did you mean any of these?',
                choices=data
            )
        
        ]
        response = inquirer.prompt(choices)
        chosen_word = response.get('choice')
        data = rest.request_thesaurus_en(chosen_word)
    elif type(data[0]) == dict:

        th = datamodel.Thesaurus()


        for word in data:
            th.addEnWord(word)
    
        

        # Ask for word choice if there is more than one option
        if len(th.words) > 1: 
            
            response_words = []
            for word in th.words:
                response_words.append((f'{word.name}  ({word.type})', word))
            questions = [
                inquirer.List(
                    'word',
                    message="Search resulted in multiple results. Which did you mean?",
                    choices=response_words,
                ),
            ]
            
            
            response = inquirer.prompt(questions)

            chosen_word = response.get('word')

        else:
            chosen_word = th.words[0]
    
    return th, chosen_word

def handle_en_ui(thesaurus: datamodel.Thesaurus, search_phrase:str) -> None:
    
    data = rest.request_thesaurus_en(search_phrase)
    
    if data == []:
        click.echo('\nNo word found. Please try again.')
        sys.exit()
    elif type(data[0]) == str:
        choices = [
            inquirer.List(
                'choice',
                message='No direct match. Did you mean any of these?',
                choices=data
            )
        ]
        response = inquirer.prompt(choices)
        chosen_word = response.get('choice')
        data = rest.request_thesaurus_en(chosen_word)

    
    for word in data:
        thesaurus.addEnWord(word)