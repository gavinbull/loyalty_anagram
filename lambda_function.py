import json, itertools, os

def gather_anagrams(input_word):
    # use itertools to find all possible combinations of word
    anagrams = sorted(set(["".join(permutation) for permutation in itertools.permutations(input_word)]))
    anagrams_list = []
    
    # create a dictionary to cross-check anagrams for words
    filename = "my_dict.txt"
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    for each_anagram in anagrams:
       if each_anagram in content:
          anagrams_list.append(each_anagram)
    return anagrams_list


def lambda_handler(event, context):
    input_word = ""                 # initiate empty string
    anagrams = ["invalid request"]  # default to invalid
    statuscode = 400                # default to forbidden
    
    # test paramter and set input word + find anagrams if valid
    try:
        input_word = event['queryStringParameters']['word']
        if input_word:
            anagrams = gather_anagrams(input_word.lower())
            statuscode = 200
    except:
        pass

    # return output in JSON
    message = {
        'anagrams': '%s' % str(anagrams)
    }
    return {
        'statusCode': statuscode,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
    }
