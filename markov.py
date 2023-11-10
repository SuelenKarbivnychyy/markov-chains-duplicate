"""Generate Markov text from text files."""

from random import choice
import random



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
    
    # print(chains)  

    return chains



def make_text(chains):
    """Return text from chains."""

    words = []

    chain_as_list = list(chains.keys()) 
    print(chain_as_list)
    choosen_key = random.choice(chain_as_list)

    random_word_from_key_value = random.choice(chains[choosen_key])

    for item in choosen_key:
        words.append(item)

    words.append(random_word_from_key_value)

    first_word_of_new_key = (choosen_key[1])
    second_word_of_new_key = random_word_from_key_value

    new_key = (first_word_of_new_key , second_word_of_new_key)
    print(f"key ouside: {new_key}")



    producing = True

    while producing:
        
        new_key = new_key
        print(f"new key on the loop:  {new_key}")

        if new_key not in chain_as_list:
            producing = False           

        else:
            first_word = (new_key[1])
            print(f"First word for new key: {first_word}")
            second_word = (random.choice(chains[new_key]))
            print(f"second word for new key: {second_word}")

            key = (first_word, second_word)
            print(f"new key is: {key}")

            if key not in chain_as_list:
                producing = False                

            else:
                word_from_list_of_words_of_key = random.choice(chains[key])            

                # for word in key:
                #     words.append(word)
                words.append(word_from_list_of_words_of_key)  

                new_key = (key[1],  random.choice(chains[key]))
                print(f"end of iratetion, the next iteration should have the key:  {new_key}")


        

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
