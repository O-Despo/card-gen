import csv
import time
import random
import datetime
import time

CARD_NUM_LENGTH = 15
NUM_OF_NAMES = 31127

class CardGenarator():
    def __init__(self, DEFAULT_CARD_TYPE = False, CARD_NUM_LENGTH = 15, NUM_OF_NAMES = 31127):
        """"""
        self.CARD_NUM_LENGTH = CARD_NUM_LENGTH
        self.NUM_OF_NAMES = NUM_OF_NAMES

        self.card_map = { 'visa': [4],
                        'mastercard': [51, 52, 53, 54],
                        'american express': [34, 37],
                        'amex': [34, 37],
                        'jbc': [34, 37],
                        'discovery': [34, 37],
                        'discover': [34, 37]
                        }

    def rand_num_w_zero(self, num_of_digits):
        digit_str = ""

        for x in range(0, num_of_digits):
            digit_str += str(random.randint(0,9))

        return digit_str

    def gen_many_cards(self, n):
        """Generate a given number of cards and output\nCalles __iter__"""
        for i in n:
            return self.__next__()

    def __iter__(self):
        """Retuns self for iteration"""
        return self

    def __next__(self):
        """calls gen_one_card"""
        return self.gen_one_card()

    def gen_one_card(self):
        """Generate a random card"""
        card_num_prefix_item = random.choice(list(self.card_map.items()))

        card_type = card_num_prefix_item[0]
        card_num_prefix = random.choice(card_num_prefix_item[1])

        len_to_gen = self.CARD_NUM_LENGTH - len(str(card_num_prefix))
        rand_card_num = self.rand_num_w_zero(len_to_gen)
        card_num = str(card_num_prefix) + str(rand_card_num) 

        with open('./posnames.csv') as names_file:
            names_source_csv = csv.reader(names_file) 
            names_source_list = list(names_source_csv) 
            names = []

            for i in range(3):
                name_index = random.randint(0, self.NUM_OF_NAMES)
                names.append(names_source_list[name_index][0])
            
            name_str = str(names[0]) + ' ' + str(names[1][0]) + ' ' + str(names[2])

        cvv = self.rand_num_w_zero(3)
        pin = self.rand_num_w_zero(4)

        current_year = time.gmtime(time.time()).tm_year

        mdate = str(random.randint(0,2)) + str(random.randint(1,9))
        ydate = str(random.randint(current_year,current_year + 5))
        date = mdate + '/' + ydate
        
        return_json = {
                'card_number': card_num,
                'name': name_str,
                'cvv': cvv,
                'pin': pin,
                'date': date
                }

        return return_json

if __name__ == "__main__":
    card_gen_instance = CardGenarator()
    card_gen_instance.gen_one_card()

    for x, i in enumerate(card_gen_instance):
        print(i)
        if x == 100: break
