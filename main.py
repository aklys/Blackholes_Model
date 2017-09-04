import numpy


def checkio(data):
    # Create list of Blackhole objects
    blackholes = []
    for i in data:
        blackholes.append(Blackhole(i))

    contine_loop = True
    if len(blackholes) == 1:
        return [(i.x, i.y, i.r) for i in blackholes]

    while contine_loop:

        blackholes_order = reorder_blackholes(blackholes)
        blackholes_temp = [i for i in blackholes]

        for calc in blackholes_order:
            if calc[0] not in blackholes_temp or calc[1] not in blackholes_temp:
                pass
            elif calc[0].check_absorb(calc[1]):
                calc[0].absorb_other(calc[1])
                blackholes_temp.remove(calc[1])
            else:
                pass

        if len(blackholes_temp) == len(blackholes) or len(blackholes_temp) == 1:
            blackholes = [i for i in blackholes_temp]
            contine_loop = False
        else:
            blackholes = [i for i in blackholes_temp]

    result = [(i.x, i.y, i.r) for i in blackholes]
    print("Output", result)
    return result


def reorder_blackholes(blackholes):
    blackholes_reordered = []

    for i in blackholes:
        nearest = None
        for j in blackholes:
            if i == j:
                pass
            else:
                blackholes_reordered.append((i, j, i.distance_between(j)))

        blackholes_reordered = sorted(blackholes_reordered, key=lambda blackhole_calc: blackhole_calc[2])

    return blackholes_reordered


class Blackhole:
    def __repr__(self):
        return str((self.x, self.y, self.r))

    def __str__(self):
        return str((self.x, self.y, self.r))

    def __init__(self, data):
        """ Expected input is a tuple/list with 3 numerical values:
            x is x coord of centre
            y is y coord of centre
            r is radius of the circle"""
        self.x = data[0]
        self.y = data[1]
        self.r = data[2]
        self.area = numpy.pi * self.r ** 2

    def distance_between(self, other):
        """Return the value between two points which happens to be the centres of the blackholes
            This help eliminate the requirement of keeping track of their different locations for future calculations"""
        if self.x == other.x and self.y == other.y:
            return 0
        else:
            return numpy.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def intersect_test(self, other):
        if (self.r + other.r) > self.distance_between(other):
            return True
        else:
            return False

    def eclipse_test(self, other):
        if self.distance_between(other) + other.r < self.r or other.distance_between(self) + self.r < other.r:
            return True
        else:
            return False

    def chord_x(self, other):
        """ Output both the x coord of the chord when both circles have y = 0 and the length of the chord"""
        distance = self.distance_between(other)
        if distance == 0:
            return 0, 0
        else:
            chord_x_pos = (distance**2 - other.r**2 + self.r**2)/(2*distance)
            chord_len = numpy.sqrt((self.r+other.r-distance)*(other.r-self.r+distance)*(distance+self.r-other.r)*(distance+self.r+other.r))/distance
            return chord_x_pos, chord_len

    def sector_angle(self, other):
        """ Output the sector angle of the intersecting line"""

        chord = self.chord_x(other)
        return numpy.arcsin((numpy.sin(numpy.radians(90))*(chord[1]/2))/self.r)*2

    def sector_area(self, other):
        angle = self.sector_angle(other)
        return (angle*self.r**2)/2

    def triangle_area(self, other):
        chord = self.chord_x(other)
        return (numpy.abs(chord[0])*chord[1])/2

    def segment_area(self, other):
        chord = self.chord_x(other)
        if self.intersect_test(other):
            if chord[0] > 0:
                return self.sector_area(other) - self.triangle_area(other)
            elif chord[0] == 0:
                return self.area * 0.5
            else:
                return self.area - (self.sector_area(other) - self.triangle_area(other))
        else:
            return 0

    def lens_area(self, other):
        return self.segment_area(other) + other.segment_area(self)

    def absorb_other(self, other):
        if self.eclipse_test(other):
            self.r = round(numpy.sqrt((self.area + other.area) / numpy.pi), 2)
            self.area = numpy.pi * self.r ** 2
        elif self.check_absorb(other):
            self.r = round(numpy.sqrt((self.area + other.area) / numpy.pi), 2)
            self.area = numpy.pi * self.r ** 2
        else:
            raise Exception("This blackhole can't absorb the other.")

    def check_absorb(self, other):
        """ Checks the following criteria are met
            * Intersection's area covers >=55% of the smaller blackhole's area
            * One blackhole is >=20% of the other blackhole """
        if self.eclipse_test(other):
            if self.area/other.area >= 1.2:
                return True
        elif self.intersect_test(other):
            lens_a = self.lens_area(other)
            if self.area/other.area >= 1.2 and lens_a/other.area >= 0.55:
                return True

        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([(2, 4, 2), (3, 9, 3)]) == [(2, 4, 2), (3, 9, 3)]
    assert checkio([(0, 0, 2), (-1, 0, 2)]) == [(0, 0, 2), (-1, 0, 2)]
    assert checkio([(4, 3, 2), (2.5, 3.5, 1.4)]) == [(4, 3, 2.44)]
    assert checkio([(3, 3, 3), (2, 2, 1), (3, 5, 1.5)]) == [(3, 3, 3.5)]
    assert checkio([[4, 3, 2],[2.1, 3.1, 1.4]]) == [(4, 3, 2),(2.1, 3.1, 1.4)]
    assert checkio([(2, 2, 3), (0, 4, 2), (4, 6, 2), (4.7, 3, 0.5)]) == [(2, 2, 3.04), (0, 4, 2), (4, 6, 2)]
    assert checkio([[4, 3, 2], [4, 3, 1.9]]) == [(4, 3, 2), (4, 3, 1.9)]
    assert checkio([[0, 0, 1], [1, 0, 1], [1.5, 0, 0.5]]) == [(0, 0, 1), (1, 0, 1.12)]
