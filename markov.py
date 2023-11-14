"""Generate Markov text from text files."""

import random
import sys



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    

    with open(file_path) as file:
        data = file.read()
        # print(data)

    return data


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """    

    chains = {}
    words = text_string.split()    

    for index in range(0, len(words)):  
              
        if index < len(words)-2:
            key_dict = words[index], words[index +1] 
            value_word = words[index +2]            

            if key_dict in chains:
                chains[key_dict].append(value_word)
            else:
                chains[key_dict] = [value_word]    
    

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    chain_as_list = list(chains.keys())     
    choosen_key = random.choice(chain_as_list)
    

    for item in choosen_key:
        words.append(item)

    key = choosen_key


    producing_text = True

    while producing_text:

        if key not in chain_as_list:
            producing_text = False           

        else:
            first_word = (key[1])           
            second_word = (random.choice(chains[key]))            

            key = (first_word, second_word)           

            words.append(second_word)
        

    return ' '.join(words)


# input_path = 'green-eggs.txt'
try:
    input_path = sys.argv[1]
except:
    input_path = 'green-eggs.txt'


# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

