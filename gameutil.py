import re

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
WORDLIST_FILENAME = "words.txt"
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def letter_score(letter):
    return SCRABBLE_LETTER_VALUES.get(letter, 0)

#
# Problem #1: Scoring a word
#


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

        The score for a word is the product of two components:

        The first component is the sum of the points for letters in the word.
        The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

        Letters are scored as in Scrabble; A is worth 1, B is
        worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """

    sum_letter_score = 0
    for letter in word.lower():
        sum_letter_score += letter_score(letter)

    wordlen = len(word)
    num_word = 7*wordlen - 3*(n-wordlen)
    if 1 > num_word:
        larger = 1
    else:
        larger = num_word

    return sum_letter_score * larger

#
# Make sure you understand how this function works and what it does!
#


def wildcard_to_regex(word: str) -> re:
    return re.compile("^" + word.replace("*", ".") + "$")

#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word_lower = word.lower()
    regex = wildcard_to_regex(word_lower)
    num_matches = len(list(filter(regex.match, word_list)))
    if num_matches == 0:
        return False

    word_freq_dict = get_frequency_dict(word_lower)
    for key in word_freq_dict.keys():
        if key not in hand.keys():
            return False
    for pair in word_freq_dict.items():
        # If letter appears more times in word than in hand
        if pair[1] > hand[pair[0]]:
            return False
    return True

#
# Problem #5: Playing a hand
#


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """

    sum = 0
    for value in hand.values():
        sum += value
    return sum


def get_input(message: str):
    return input(message).strip().lower()
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # wordlist: list of strings
    wordlist = []
    with open(WORDLIST_FILENAME, 'r') as inFile:
        for line in inFile:
            wordlist.append(line.strip().lower())

    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------
