# Thesaurus
A small cli application that let's you look up synonyms for both English and Swedish words. This tool is written in python and uses `click` and `textual`. 


## Installation

1. Clone repo.
2. Get Merriam-Webster API key and save it in `.env` file as `MW_API_KEY`.
3. Run `pip install .` in root directory.


## Usage

Run

`th [OPTIONS] SEARCH_PHRASE`

or

`thesaurus [OPTIONS] SEARCH_PHRASE`


**Options**:

  `-en`, `--english` (Default)

  `-sv`, `--svenksa`

 ` -ui`, `--user-interface` / `-pt`, `--plain-text` (ui comes by default)