import csv
import time
import random
import datetime
import time

CARD_NUM_LENGTH = 15
NUM_OF_NAMES = 31127

class cardGenarator():
    def __init__(self, CARD_NUM_LENGTH = 15, NUM_OF_NAMES = 31127):
        self.CARD_NUM_LENGTH = CARD_NUM_LENGTH
        self.NUM_OF_NAMES = NUM_OF_NAMES

        self.card_map = {
                'visa': [4],
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
    
    def get_card_in(self):
        card_issuer = input("Choose a card type: Visa, Mastercard, American Express, JBC, or Discovery")
        card_issuer = card_issuer.lower()
        card_num_prefix_list = card_map[card_issuer]

    def gen_card(self):
        card_num_prefix_list = random.choice(list(self.card_map.items()))
        card_num_prefix = random.choice(card_num_prefix_list[1])

        len_to_gen = self.CARD_NUM_LENGTH - len(str(card_num_prefix))
        card_num = self.rand_num_w_zero(len_to_gen)

        with open('./posnames.csv') as names_file:
            names_csv = csv.reader(names_file) 
            names_list = list(names_csv) 
            names = []

            for i in range(3):
                name_index = random.randint(0, self.NUM_OF_NAMES)
                names.append(names_list[name_index][0])
            
            name_str = str(names[0]) + ' ' + str(names[1][0]) + ' ' + str(names[2])

        cvv = rand_num_w_zero(3)
        pin = rand_num_w_zero(4)

        current_year = time.gmtime(time.time()).tm_year

        mdate = str(random.randint(0,2)) + str(random.randint(1,9))
        ydate = str(random.randint(current_year,current_year + 5))
        date = mdate + '/' + ydate
        
        if format_json:
            return_item = {
                    'card_number': card_num,
                    'name': name_str,
                    'cvv': cvv,
                    'pin': pin,
                    'date': date
                    }
        else:
            return_item  

        return(card_num, name_str, cvv, pin, date)


