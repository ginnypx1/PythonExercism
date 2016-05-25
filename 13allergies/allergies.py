class Allergies(object):
    """Results of an allergy test"""
    allergens = {
        1: 'eggs',
        2: 'peanuts',
        4: 'shellfish',
        8: 'strawberries',
        16: 'tomatoes',
        32: 'chocolate',
        64: 'pollen',
        128: 'cats'
    }

    def __init__(self, score):
        self.score = score
        self.lst = self.lst()

    def lst(self):
        allergen_list = []
        # sort allergens by key, low to high
        allergens_vals = sorted(self.allergens) 
        # while there is still a score
        while self.score > 0:
            # find the maximum allergy value that is still lower than the score
            allergy = max([val for val in allergens_vals if val <= self.score])
            # add that item to allergen_list
            allergen_list.append(self.allergens[allergy])
            # decrease the score
            self.score -= allergy
        return allergen_list

    def is_allergic_to(self, item):
        '''asks if patient is allergic to a specific item'''
        return item in self.lst
