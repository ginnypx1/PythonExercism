import itertools


KINDERGARTEN_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 
                         'Eve', 'Fred', 'Ginny', 'Harriet', 
                         'Ileana', 'Joseph', 'Kincaid', 'Larry']

PLANT_CODE = {
    'V': 'Violets',
    'R': 'Radishes',
    'G': 'Grass',
    'C': 'Clover'
}


class Garden(object):
    """Given a diagram:
        ```plain
        [window][window][window]
        ........................ # each dot represents a styrofoam cup
        ........................
        ```

        The instructions: "Each child gets 4 cups, two on each row. 
        The children are assigned to cups in alphabetical order.""

        And the plants: "Violets, Radishes, Grass and Clover"

        can tell you which plants each child in the kindergarten class is responsible for.

        var seeds: a string composed of the first letter of each plant representing the rows in the garden (ex: "VVCCGG\nVVCCGG")
        optional var students: a list of the students in the class
    """
    def __init__(self, seeds, students=KINDERGARTEN_STUDENTS):
        self.seeds = seeds
        self.students = sorted(students)
        self.garden_bed = self.plant()

    def plant(self):
        '''Given the seeds, plants the garden bed'''
        i = 0
        j = 0
        row_one = []
        row_two = []
        final_bed = []
        # given seeds, split at new line
        row_a, row_b = self.seeds.split('\n')
        # divide into splits of two
        while i < len(row_a):
            row_a = list(row_a)
            row_one.append(row_a[i:i+2])
            i += 2

        while j < len(row_b):
            row_b = list(row_b)
            row_two.append(row_b[j:j+2])
            j += 2
        # group into fours
        garden_rows = list(zip(row_one, row_two))
        # flatten the lists
        for each in garden_rows:
            final_bed.append(list(itertools.chain.from_iterable(each)))
        # return a dictionary assigning the plants to each student
        return dict(zip(self.students, final_bed))

    def plants(self, student):
        '''Given the name of a student, returns what seeds they planted'''
        plant_list = []
        for plant in self.garden_bed[student]:
            plant_list.append(PLANT_CODE[plant])
        return plant_list
