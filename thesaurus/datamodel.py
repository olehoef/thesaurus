import json, uuid



class Thesaurus():
    def __init__(self):
        self.words = []

    def addEnWord(self, word_dict):
        #* Prepare data

        # Meta data
        word_name = word_dict.get('meta').get('id')
        word_uuid = word_dict.get('meta').get('uuid')
        word_type = word_dict.get('fl')

        # Senses
        senses_list = word_dict.get('def')[0].get('sseq')
        word_senses = []
        for sense in senses_list:
            sense_dict = sense[0][1]
            definition = sense_dict.get('dt')[0][1]

            # Associated words
            associations_names = ['syn_list', 'rel_list', 'sim_list']
            associations_store = {} # stores the association matrices before they are assigned to a new Sense
            for association in associations_names:
                association_list = sense_dict.get(association, [])
                association_matrix = []
                if association_list != []:
                    for word_list in association_list:
                        word_collection = []
                        for word_dict in word_list:
                            word_collection.append(word_dict.get('wd'))
                        association_matrix.append(word_collection)
                associations_store[association] = association_matrix
           

            # Create sense
            new_sense = Sense(
                definition=definition,
                syns=associations_store.get('syn_list'),
                rels=associations_store.get('rel_list'),
                sims=associations_store.get('sim_list')
            )
            word_senses.append(new_sense)

        # Create Word
        new_word = Word(
            name=word_name,
            uuid=word_uuid,
            type=word_type,
            senses=word_senses,
            examples=None,
            idioms=None
        )

        # Add word to thesaurus
        self.words.append(new_word)
        

    def addSvWord(self, word_name, word_dict):
        sense = Sense(
            definition=word_dict.get('definition', ''),
            syns=word_dict.get('synonyms', None),
            rels=[],
            sims=[]
        )
        examplesList = word_dict.get('examples', None)
        idiomsList = word_dict.get('idioms', None)
        new_word = Word(
            name=word_name,
            uuid=uuid.uuid4(),
            type=None,
            senses=[sense],
            examples=examplesList if  examplesList != '' else None,
            idioms=idiomsList if idiomsList != '' else None,

        )
        self.words.append(new_word)


class Word():

    def __init__(self, name, uuid, type, senses, examples, idioms):
        self.name=name # meta.id
        self.uuid=uuid # meta.uuid
        self.type=type # fl
        self.senses=senses # def.sseq[i][0][0]
        self.examples=examples
        self.idioms=idioms



class Sense():

    def __init__(self, definition, syns, rels, sims):
        self.definition = definition # def.sseq[i][0][1].dt[0][1]
        self.syns=syns # def.sseq[i][0][1].syn_list
        self.rels=rels # def.sseq[i][0][1].rel_list
        self.sims=sims # def.sseq[i][0][1].sim_list





