import random
import json
import os
import numpy as np #need to install
from datetime import date, datetime


def open_file(name):
    """
    Opens a Json file and returns the dict inside.
    """
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, name)
    with open(my_file) as file:
        return json.load(file)

def __answer(tag_index, intents_list):
    return random.choice(intents_list[tag_index]['responses'])

def __find_tag(sentense, intents_list):
    """ 
    Find the appropriate tag for the sentence in param and returns it.
    """
    list_score_tags = []
    for dic in intents_list:
        list_score_tags.append(__compare_patterns(sentense, dic))
    index_max_value = list_score_tags.index(max(list_score_tags))
    return (index_max_value, intents_list[index_max_value]['tag'])

def __compare_patterns(sentense, dic):
    """ 
    Compare the sentence of the user with the differnts patterns.
    Returns the score based on the frequency of each words in the sentence.
    """
    list_words = sentense.split()
    list_freq = [0 for i in range(len(list_words))]
    for index in range(len(list_words)):
        for elem in dic['patterns']:
            for wrd in elem.split():
                if list_words[index] == wrd:
                    list_freq[index] += 1
        if dic['tag'] == list_words[index]:
            list_freq[index] += 10
    return np.sum(list_freq)

def __get_current_date():
    months = {1 : 'January',  2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May',
          6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'}
    return f"{date.today().day} {months[date.today().month]} {date.today().year}"

def __get_current_time():
    return datetime.now().strftime("%H:%M:%S")