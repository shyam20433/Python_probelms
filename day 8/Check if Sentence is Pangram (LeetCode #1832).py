import re
def pangram(sentence):
    sentence=sentence.lower()
    sentence= re.sub(r'[^a-z]','', sentence)
    return len(list(dict.fromkeys(sentence)))==26


print((pangram("the quick brown fox jumps over the lazy dog")))