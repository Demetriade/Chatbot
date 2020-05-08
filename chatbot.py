import random
import json
import os
import numpy as np #need to install
from datetime import date, datetime


class Chatbot:

    def __init__(self):
        self.intents_list = self.__open_file('intents.json')['intents']
    
    def run(self):
        running = True
        print('----------------------------------------------------')
        while(running):
            answer = input('Ask anything : ')
            tup = self.__find_tag(answer.lower())
            print(self.__answer(tup[0]))

            if answer in ['exit', 'stop', 's']:
                running = False
                print('Thanks for the chat! Have a nice day!\n')

    def __open_file(self, name):
        """
        Opens a Json file and returns the dict inside.
        """
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, name)
        with open(my_file) as file:
            return json.load(file)

    def __answer(self, tag_index):
        answ = random.choice(self.intents_list[tag_index]['responses'])
        if tag_index == 5:
            answ.join(self.__get_current_time())
        elif tag_index == 6:
            answ.join(self.__get_current_date())
        return answ

    def __find_tag(self, sentense):
        """ 
        Find the appropriate tag for the sentence in param and returns it.
        Returns tuple of (index, tag)
        """
        list_score_tags = []
        for dic in self.intents_list:
            list_score_tags.append(self.__compare_patterns(sentense, dic))
        index_max_value = list_score_tags.index(max(list_score_tags))
        return (index_max_value, self.intents_list[index_max_value]['tag'])

    def __compare_patterns(self, sentense, dic):
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

    def __get_current_date(self):
        months = {1 : 'January',  2 : 'February', 3 : 'March', 4 : 'April', 5 : 'May',
            6 : 'June', 7 : 'July', 8 : 'August', 9 : 'September', 10 : 'October', 11 : 'November', 12 : 'December'}
        return f"{date.today().day} {months[date.today().month]} {date.today().year}"

    def __get_current_time(self):
        return datetime.now().strftime("%H:%M:%S")