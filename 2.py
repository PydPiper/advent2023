'''
--- Day 2: Cube Conundrum ---
You're launched high into the atmosphere! The apex of your trajectory just barely reaches the surface of a large island floating in the sky. You gently land in a fluffy pile of leaves. It's quite cold, but you don't see much snow. An Elf runs over to greet you.

The Elf explains that you've arrived at Snow Island and apologizes for the lack of snow. He'll be happy to explain the situation, but it's a bit of a walk, so you have some time. They don't get many visitors up here; would you like to play a game in the meantime?

As you walk, the Elf shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, the Elf will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
'''

#read file
#split line
#split :
#split ;
#split ,
#split " " into val and color
#compare to max per color, if over max break to next line in file
#if all sets on line are below max and id to sum

import unittest
from unittest import mock
import functools

def yieldLineFromFile(filename:str) -> str:
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def mainPart1(filename:str) -> int:
    total = 0
    maxCubes = {"red":12, "blue":14, "green":13}

    for line in yieldLineFromFile(filename):
        game, gameString = line.split(":")
        gameID = game.split()[1]
        gameSets = gameString.split(";")
        valid = True
        for gameSet in gameSets:
            combos = gameSet.split(",")
            for combo in combos:
                val, color = combo.split()
                if int(val) > maxCubes[color]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            total += int(gameID)
    return total

def mainPart2(filename:str) -> int:
    total = 0

    for line in yieldLineFromFile(filename):
        game, gameString = line.split(":")
        gameID = game.split()[1]
        gameSets = gameString.split(";")
        minCubes = {}
        for gameSet in gameSets:
            combos = gameSet.split(",")
            for combo in combos:
                val, color = combo.split()
                val = int(val)
                if color not in minCubes.keys():
                    minCubes[color] = val
                if val > minCubes[color]:
                    minCubes[color] = val
        gameTotal = functools.reduce(lambda a, b: a*b, minCubes.values())
        total += gameTotal
    return total

class TestMain(unittest.TestCase):

    def test_MainPart1(self):

        with mock.patch('__main__.yieldLineFromFile', return_value=['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']):
            rv = mainPart1('fake.data')
            self.assertEqual(1, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=[
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']):
            rv = mainPart1('fake.data')
            self.assertEqual(8, rv)

    def test_MainPart2(self):

        with mock.patch('__main__.yieldLineFromFile', return_value=['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']):
            rv = mainPart2('fake.data')
            self.assertEqual(6*4*2, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=[
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']):
            rv = mainPart2('fake.data')
            self.assertEqual(6*4*2+4*3*1+13*20*6+14*15*3+6*3*2, rv)

if __name__ == '__main__':
    FILENAME = '2.data'
    RUNTEST = False

    if RUNTEST:
        unittest.main()
    else:
        print(f'part1 = {mainPart1(FILENAME)}')
        print(f'part2 = {mainPart2(FILENAME)}')