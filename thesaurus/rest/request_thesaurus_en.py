import requests, threading, itertools, sys, time, dotenv, os
from thesaurus import utils


dotenv.load_dotenv('.env')

def request_thesaurus_en(search_phrase):
    base_url = 'https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}'
    API_KEY = os.getenv("MW_API_KEY")
    params = {'key': API_KEY}

    
    url = base_url.format(search_phrase)
 
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
    response = requests.get(url, params=params)
    done = True
    

   
    if response.status_code == 200:
        data = response.json()
        return data
    
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None


