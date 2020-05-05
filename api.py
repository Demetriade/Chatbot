import random
import json
import os
from datetime import date


def open_file(name):
    """
    Opens a Json file and returns the dict inside.
    """
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, name)
    with open(my_file) as file:
        return json.load(file)

def find_tag(sentense):
    """ 
    Find the appropriate tag for the sentence in param and returns it.
    """

def __compare_patterns(sentense):
    """ 
    Compare the sentence of the user with the differnts patterns.
    Returns list of the score of each words in the sentence.
    """

def get_current_date():
    return date.today()