import json
import itertools

def gather_anagrams(input_word):
    anagrams_list = [ "".join(all_permutations) for all_permutations in itertools.permutations(input_word) if len(all_permutations) == len(input_word) ]
    return anagrams

def lambda_handler(event, context):
    return event
    # define input word and set output anagrams
    input_word = ""
    anagrams = ["invalid request"]
    try:
        input_word = event['queryStringParameters']['word']
        if input_word:
            # if word is present, find anagrams
            anagrams = gather_anagrams(input_word)
    except:
        pass

    # return output in JSON
    message = {
        'anagrams': '%s' % str(anagrams)
    }

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(message)
    }
