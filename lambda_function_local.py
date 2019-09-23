import json, itertools, os
from nltk.corpus import wordnet as wn

def gather_anagrams(input_word):
    # use itertools to find all possible combinations of word
    anagrams = sorted(set(["".join(permutation) for permutation in itertools.permutations(input_word)]))
    anagrams_list = []
    for each_word in anagrams:
        if nw.synsets(each_word):
            anagrams_list.append(each_word)
    return anagrams_list

def lambda_handler():
    input_word = "iceman"                 # initiate empty string
    anagrams = ["invalid request"]  # default to invalid
    statuscode = 400                # default to forbidden
    anagrams = gather_anagrams(input_word)
    statuscode = 200

    # return output in JSON
    message = {
        'anagrams': '%s' % str(anagrams)
    }
    return {
        'statusCode': statuscode,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
    }

