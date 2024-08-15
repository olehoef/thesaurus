import requests, threading, itertools, sys, time, json
from thesaurus import utils



def request_words_sv(search_phrase):
    base_url = 'https://synonymord.se/api/'

    word_param = {'w': search_phrase}

 
    # Loading animation
    done = False
    def animateProcessing():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rprossessing request...' + c)
            sys.stdout.flush()
            time.sleep(0.1)
    t = threading.Thread(target=animateProcessing)
    t.start()

    # GET request
    response = requests.get(base_url, params=word_param)
    done = True
    

    if response.status_code == 200:
        json_data = response.text.lstrip('\ufeff')

        data = json.loads(json_data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


def request_synonyms_sv(word):
    base_url = 'https://synonymord.se/api/'

    param = {'q': word}

 
    # Loading animation
    done = False
    def animateProcessing():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rprossessing request...' + c)
            sys.stdout.flush()
            time.sleep(0.1)
    t = threading.Thread(target=animateProcessing)
    t.start()

    # GET request
    response = requests.get(base_url, params=param)
    done = True
    

    if response.status_code == 200:
        json_data = response.text.lstrip('\ufeff')

        data = json.loads(json_data)
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None