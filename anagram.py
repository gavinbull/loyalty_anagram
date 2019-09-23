import json

def gather_anagrams(input_word):
    if len(input_word) <=1:
        return input_word
    else:
        anagrams = []
        for perm in gather_anagrams(input_word[1:]):
            for i in range(len(input_word)):
                anagrams.append(perm[:i] + input_word[0:1] + perm[i:])
        return anagrams

def lambda_handler(event, context):
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
