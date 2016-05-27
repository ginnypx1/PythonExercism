NORTH = "NORTH"
EAST = "EAST"
SOUTH = "SOUTH"
WEST = "WEST"


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
            self.y += 1
            self.coordinates = (self.x, self.y)
        if self.bearing == SOUTH:
            self.y -= 1
            self.coordinates = (self.x, self.y)
        if self.bearing == EAST:
            self.x += 1
            self.coordinates = (self.x, self.y)
        if self.bearing == WEST:
            self.x -= 1
            self.coordinates = (self.x, self.y)
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

