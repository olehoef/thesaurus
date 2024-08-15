from thesaurus import datamodel, rest
import inquirer

def handle_sv_input(thesaurus, search_phrase) -> datamodel.Word:
    words_res = rest.request_words_sv(search_phrase)
    words=words_res.get('words', [])
    for word in words:
        q_res = rest.request_synonyms_sv(word)                
        thesaurus.addSvWord(word, q_res)

    response_words = []
    for word in thesaurus.words:
        response_words.append((word.name, word))
    questions = [
        inquirer.List(
            'word',
            message="Search resulted in multiple results. Which did you mean?",
            choices=response_words,
        ),
    ]
    
    
    response = inquirer.prompt(questions)

    chosen_word = response.get('word')
    return chosen_word

def handle_sv_ui(thesaurus, search_phrase):
    words_res = rest.request_words_sv(search_phrase)
    words=words_res.get('words', [])
    for word in words:
        q_res = rest.request_synonyms_sv(word)                
        thesaurus.addSvWord(word, q_res)