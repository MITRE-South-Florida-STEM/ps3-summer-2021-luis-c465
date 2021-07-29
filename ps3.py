# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Luis Canada
# Collaborators : None
# Time spent    : <total time>

import math
import random
import string
from gameutil import *

HAND_SIZE = 7


def display_hand(hand: dict) -> None:
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#


def deal_hand(n: int) -> dict:
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand["*"] = 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand: dict, word: str) -> dict:
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    updated_hand = hand.copy()
    for letter in word.lower():
        value = updated_hand.get(letter, None)
        if value != None:
            if value == 1:
                updated_hand.pop(letter)
            else:
                updated_hand[letter] -= 1
    return updated_hand


def play_hand(hand: int, word_list: list) -> int:
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """

    # Keep track of the total score
    total_score = 0
    hand = deal_hand()

    # As long as there are still letters left in the hand:
    while hand.keys() != 0:
        # Display the hand
        display_hand(hand)

        # Ask user for input
        input_msg = "Enter word, or \"!!\" to indicate that you are finished: "
        user_input = input(input_msg)

        # If the input is two exclamation points:
        if user_input == "!!":
            # End the game (break out of the loop)
            break

        # Otherwise (the input is not two exclamation points):
        # If the word is valid:
        if is_valid_word(user_input):

            # Tell the user how many points the word earned,
            # and the updated total score
            word_score = get_word_score(user_input)
            total_score += word_score
            print(
                f"\"{user_input}\" earned {word_score} points. Total: {total_score} points ")

        # Otherwise (the word is not valid):
        else:
            # Reject invalid word (print a message)
            print("That is not a valid word. Please choose another word.")

        # update the user's hand by removing the letters of their inputted word
        hand = update_hand(hand, user_input)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    print(f"Total score: {total_score} points")

    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
#


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand: dict, letter: str) -> dict:
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    pass  # TO DO... Remove this line when you implement this function


def play_game(word_list: list) -> int:
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    # TO DO... Remove this line when you implement this function
    num_of_hands = input("Enter total number of hands: ")
    total_score = 0


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
