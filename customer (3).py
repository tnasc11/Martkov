import random
import itertools

LOCATION = ['entry', 'dairy', 'drinks', 'fruit', 'spices', 'checkout']
tm = {'entry': {'entry': 0.0,
                    'dairy': 0.0,
                    'drinks': 0.0,
                    'fruit': 0.0,
                    'spices': 0.0,
                    'checkout': 0.0},
          'dairy': {'entry': 0.2875755540631296,
                    'dairy': 0.7369870713884205,
                    'drinks': 0.010897501799115862,
                    'fruit': 0.09586347908147216,
                    'spices': 0.19309137217446673,
                    'checkout': 0.0},
          'drinks': {'entry': 0.15352585627938214,
                     'dairy': 0.05851602023608769,
                     'drinks': 0.5985401459854015,
                     'fruit': 0.05481283422459893,
                     'spices': 0.16300541228907992,
                     'checkout': 0.0},
          'fruit': {'entry': 0.3774345198119543,
                    'dairy': 0.049803260258572235,
                    'drinks': 0.08789966073815153,
                    'fruit': 0.5972003774771941,
                    'spices': 0.09089461954791468,
                    'checkout': 0.0},
          'spices': {'entry': 0.18146406984553393,
                     'dairy': 0.051320966835300734,
                     'drinks': 0.08697440115143415,
                     'fruit': 0.05064485687323057,
                     'spices': 0.402419611588666,
                     'checkout': 0.0},
          'checkout': {'entry': 0.0,
                       'dairy': 0.10337268128161889,
                       'drinks': 0.21568829032589698,
                       'fruit': 0.20147845234350426,
                       'spices': 0.15058898439987264,
                       'checkout': 1.0}}


class Customer:
    
    def __init__(self):
        import itertools
        id_iter = itertools.count()
        self.identifier = next(id_iter)
        self.location = 'entry'
        self.status = 'active'

    def __repr__(self):
        return f'<Customer {self.identifier} moves toward {self.location}>'
    
    def move_location(self):
        while self.location != 'checkout':
                probs = tm[self.location]
                next_state = random.choices(LOCATION, probs)[0]
                self.location = next_state
        return self.location


#test_customer = Customer()
#print(test_customer)