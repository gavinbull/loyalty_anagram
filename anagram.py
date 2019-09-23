import json, itertools

def gather_anagrams(input_word):
    anagrams = sorted(set(["".join(permutation) for permutation in itertools.permutations(input_word)]))
    return anagrams

def lambda_handler(event, context):
    # define input word and set output anagrams
    input_word = ""
    anagrams = ["invalid request"]
    statuscode = 400
    try:
        input_word = event['queryStringParameters']['word']
        if input_word:
            # if word is present, find anagrams
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
