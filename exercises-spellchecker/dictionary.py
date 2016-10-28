"""
We represent an English dictionary by using a python set
(don't confuse our English definition of dictionary
with a python dictionary here--anytime you see the word
"dictionary", we mean English dictionary).
"""


def load(dictionary_name):
    """
    Opens the file called `dictionary_name` and returns
    the set of words in that file.

    Hint: call the strip() method on a word to trim surrounding
    whitespace and newlines.

    Each line in the file contains exactly one word.
    """
    global counter
    counter = 0 
    wordlist=[[] for x in range(2000)]
    with open(dictionary_name) as words:
        for word in words:
            stripword = word.strip()
            wordhash = hash(stripword) % 2000
            wordlist[wordhash].append(stripword)
            counter = counter + 1
    return wordlist


def check(dictionary, word):
    """
    Returns True if `word` is in the English `dictionary`.
    """
    return (word in dictionary[(hash(word.lower())%2000)])

def size(dictionary):
    """
    Returns the number of words in the English `dictionary`.
    """
    return counter

def unload(dictionary):
    """
    Removes everything from the English `dictionary`.
    """
    for subdict in dictionary:
        for word in subdict:
            subdict.remove(word)
        dictionary.remove(subdict)
