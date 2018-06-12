import json
import sys
from random import randint
from collections import OrderedDict
from copy import deepcopy
from collections import Counter

start = sys.argv[1]
name = sys.argv[2]
races_count = int(sys.argv[3])


def generate_crash_chance():
    return randint(0, 1)


filename = 'cars.json'


def open_file(filename):
    if isinstance(filename, str):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    else:
        return filename


def write_json(data):
    with open('result.json', 'a+') as f:
        json.dump(data, f)


class Car:
    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return '{} {} with max speed {}'.format(self.car, self.model, self.max_speed)


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return '{} has {}'.format(self.name, self.car)

    def __repr__(self):
        return '{} has {}.'.format(self.name, self.car)


class Race:
    drivers_in_race = dict()
    with_crash = dict()
    without_crash = dict()

    def __init__(self, drivers, crash_chance):
        self.drivers = drivers
        self.crash_chance = crash_chance

    def result(self):
        for i in self.drivers:
            self.drivers_in_race[i.name] = 1

        if self.crash_chance == 0:
            points_of_drivers = dict()
            for i in range(4, 1, -1):
                chousen_driver = self.drivers_in_race.popitem()
                points_of_drivers[chousen_driver[0]] = 2 * i
            self.drivers_in_race.update(points_of_drivers)

            d_sorted_by_value = OrderedDict(
                sorted(self.drivers_in_race.items(), key=lambda x: x[1], reverse=True))
            first_3 = {k: d_sorted_by_value[k]
                       for k in list(d_sorted_by_value)[:3]}

            self.without_crash = deepcopy(first_3)

            s = [(k, first_3[k])
                 for k in sorted(first_3, key=first_3.get, reverse=True)]

            for key, value in s:
                print('{} - {}'.format(key, value))

            return self.without_crash

        if self.crash_chance == 1:
            for key, value in self.drivers_in_race.items():
                self.drivers_in_race[key] = generate_crash_chance()

            crashed_drivers = deepcopy(self.drivers_in_race)

            for key, value in self.drivers_in_race.items():
                if value != 0:
                    del crashed_drivers[key]

            for key in crashed_drivers.keys():
                if key in self.drivers_in_race:
                    del self.drivers_in_race[key]

            points_of_drivers = dict()
            for i in range(4, 1, -1):
                try:
                    chousen_driver = self.drivers_in_race.popitem()
                    points_of_drivers[chousen_driver[0]
                                      ] = 2 * i * chousen_driver[1]
                except KeyError:
                    pass

            self.drivers_in_race.update(points_of_drivers)

            d_sorted_by_value = dict(
                sorted(self.drivers_in_race.items(), key=lambda x: x[1], reverse=True))

            first_3 = {k: d_sorted_by_value[k]
                       for k in list(d_sorted_by_value)[:3]}

            s = [(k, first_3[k])
                 for k in sorted(first_3, key=first_3.get, reverse=True)]
#            print('S', s)
            for key, value in s:
                if key in crashed_drivers.keys():
                    continue
                else:
                    print('{} - {}'.format(key, value))

            print()

            for key in crashed_drivers.keys():
                print('Unfortunately, {} has crashed.'.format(key))
            self.without_crash = deepcopy(first_3)

            return self.without_crash


class Championship:
    points = []
    scores = dict()
    final_result = dict()

    def __init__(self, name, races_count):
        self.name = name
        self.race_count = races_count

    def generate_race(self):
        race = Race(create_drivers(), generate_crash_chance())
        return race.result()

    def top3(self):
        for i in range(1, self.race_count + 1):
            print('Race #{}'.format(i))
            print('###### START ######')
            a = self.generate_race()
            # print(a)
            self.points.append(a)
#        print('Points', self.points)
        self.scores[self.name] = self.points
        write_json(self.scores)
        c = Counter()
        for d in self.points:
            c.update(d)
        print('Total championship standings:')
        for key, value in dict(c).items():
            print('{} - {}'.format(key, value))


def create_drivers():
    data = open_file(filename)
    drivers = []
    for i in data['people']:
        drivers.append(Driver(i['name'], Car(
            i['car'], i['model'], i['max_speed'])))

    return drivers


if start =='start':
    champ = Championship(name,races_count)
    print(champ.top3())
