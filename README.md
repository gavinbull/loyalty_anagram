# loyalty_anagram

## Service

Web-service to provide all possible anagrams for a given word

The function is hosted in AWS Lambda (python function) and served out via AWS API gateway

API endpoint URL:  https://r8zw8hu6zf.execute-api.us-east-1.amazonaws.com/test/anagram

## Security

API KEY for testing:   ZSvI1Bxj5r89aelpGm5YH31t3PVjGpaZ3woHHbd0

## Usage

curl -H 'X-Api-Key:ZSvI1Bxj5r89aelpGm5YH31t3PVjGpaZ3woHHbd0' 'https://r8zw8hu6zf.execute-api.us-east-1.amazonaws.com/test/anagram?word=ciNeMa'

{"anagrams": "['anemic', 'cinema', 'iceman']"}

## Unit Test

test_lambda_function.py

