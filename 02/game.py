#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    return [random.choice(POUCH) for _ in range(0, NUM_LETTERS)]
    
def input_word(draw):
    word = raw_input("Your word: ").upper()
    if _validation(word, draw):
        print(calc_word_value(word))
        print("YOU SHALL PASS")
    else:
        print("YOU SHALL NOT PASS")


def _validation(word, draw):
    for letter in word:
        if letter not in draw:
            raise(ValueError)
            print("Your letters are not in the draw")
            return False 
    return _validate_from_dict(word)
            
def _validate_from_dict(word):
    with open("dictionary.txt") as f:
        all_words = [words.strip() for words in f.read().split()]
    for all_word in all_words:
        if all_word.upper() == word:
            return True
    raise(ValueError)
    print("Your word doesn't exist")
    return False


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def _get_permutations_draw(word):
    pass

def get_possible_dict_words(word):
    pass



def main():
    draw = draw_letters()
    print("Your letters are: {}".format(" ".join(draw)))

    word = input_word(draw)



if __name__ == "__main__":
    main()
