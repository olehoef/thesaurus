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

    # Make a GET request
    response = requests.get(base_url, params=word_param)
    done = True
    

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
       # Remove BOM if present
        json_data = response.text.lstrip('\ufeff')

        # Parse JSON data
        data = json.loads(json_data)
        return data
    else:
        # Print an error message if the request was not successful
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

    # Make a GET request
    response = requests.get(base_url, params=param)
    done = True
    

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
       # Remove BOM if present
        json_data = response.text.lstrip('\ufeff')

        # Parse JSON data
        data = json.loads(json_data)
        return data
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")
        return None