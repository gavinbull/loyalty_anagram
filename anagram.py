import json, itertools, os

def gather_anagrams(input_word):
    
    # use itertools to find all possible combinations of word
    anagrams = sorted(set(["".join(permutation) for permutation in itertools.permutations(input_word)]))
    my_dict = enchant.Dict("en_US")
    for each_word in anagrams:
        if my_dict.check(each_word):
            my_dict.append(each_word)
    return my_dict

def lambda_handler(event, context):
    input_word = ""                 # initiate empty string
    anagrams = ["invalid request"]  # default to invalid
    statuscode = 400                # default to forbidden
    
    # test paramter and set input word + find anagrams if valid
    try:
        input_word = event['queryStringParameters']['word']
        if input_word:
            anagrams = gather_anagrams(input_word)
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
