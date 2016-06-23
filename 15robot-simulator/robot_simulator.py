import operator

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)


class Robot(object):
    """Simulates a robot with three possible movements: left turn, right turn and advance"""
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)
        self.bearing = bearing

    def turn_right(self):
        """Simulates a right turn"""
        right_turns = {
            NORTH: EAST,
            EAST: SOUTH,
            SOUTH: WEST,
            WEST: NORTH
        }
        self.bearing = right_turns[self.bearing]
        return self.bearing

    def turn_left(self):
        """Simulates a left turn"""
        left_turns = {
            NORTH: WEST,
            WEST: SOUTH,
            SOUTH: EAST,
            EAST: NORTH
        }
        self.bearing = left_turns[self.bearing]
        return self.bearing

    def advance(self):
        """Simulates an advance movement"""
        if self.bearing == NORTH:
            self.coordinates = tuple(map(operator.add, self.coordinates, NORTH))
        if self.bearing == SOUTH:
            self.coordinates = tuple(map(operator.add, self.coordinates, SOUTH))
        if self.bearing == EAST:
            self.coordinates = tuple(map(operator.add, self.coordinates, EAST))
        if self.bearing == WEST:
            self.coordinates = tuple(map(operator.add, self.coordinates, WEST))
        return self.coordinates

    def simulate(self, pathstring):
        """Carries out a string of simulated movements"""
        for move in pathstring:
            if move == 'R':
                self.turn_right()
            if move == 'L':
                self.turn_left()
            if move == 'A':
                self.advance()

