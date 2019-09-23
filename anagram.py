import json, itertools

def gather_anagrams(input_word):
    # use itertools to find all possible combinations of word
    anagrams = sorted(set(["".join(permutation) for permutation in itertools.permutations(input_word)]))
    return anagrams

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
