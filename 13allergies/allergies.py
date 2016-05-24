# I'm not sure I understand from the directions what lst is asking for... 
# My understanding based on the tests is either return the allergy with the specific value or all.
# Another version would be to return everything less than the score, but then the 'peanuts only' test would include an allergy to eggs.

class Allergies:
    """Results of an allergy test"""
    allergins = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score

    @property
    def lst(self):
        allergin_list = []
        for key, value in self.allergins.items():
            if value == self.score:
                allergin_list.append(key)
        if self.score == 255:
            for key in self.allergins:
                allergin_list.append(key)
        return allergin_list

    def is_allergic_to(self, item):
        '''asks if patient is allergic to a specific item'''
        if self.allergins[item] <= self.score:
            return True
        else:
            return False
