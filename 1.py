'''
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
'''

import unittest
from unittest import mock
import re

# yield line from file
# loop fwd till you see a numeric
# loop backward till you see a numeric
# combine str and convert to int
# add int to running total

def yieldLineFromFile(filename:str) -> str:
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def mainPart1(filename:str) -> int:
    """time complexity O(lc) where, 
    l = number of lines in file
    c = number of char in line
    space complecity O(1)

    :param filename: data file
    :type filename: str
    :return: sum of each line's 1st and last numeric value
    :rtype: int
    """
    total = 0

    for line in yieldLineFromFile(filename):
        char1 = ''
        char2 = ''
        for char in line:
            if char.isnumeric():
                char1 = char
                break
        for char in line[::-1]:
            if char.isnumeric():
                char2 = char
                break
        num = int(char1 + char2)
        total += num
    return total

def mainPart2(filename:str) -> int:
    """time complexity O(lc) where, 
    l = number of lines in file
    c = number of char in line
    space complecity O(1)

    :param filename: data file
    :type filename: str
    :return: sum of each line's 1st and last numeric value
    :rtype: int
    """
    total = 0

    char2num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    char2numBackwards = {k[::-1]:v for k, v in char2num.items()}


    char2numRegEx = re.compile('(' + '|'.join(char2num.keys()) + ')', re.IGNORECASE)
    char2numRegExBackwards = re.compile('(' + '|'.join(char2numBackwards.keys()) + ')', re.IGNORECASE)
    with open('1convert.data', 'w') as f:
        for line in yieldLineFromFile(filename):
            char1 = ''
            char2 = ''
            templine = re.sub(char2numRegEx, lambda match: char2num[match.group().lower()], line)
            f.write(line + '\n')
            for char in templine:
                if char.isnumeric():
                    char1 = char
                    break
            templine = re.sub(char2numRegExBackwards, lambda match: char2numBackwards[match.group().lower()], line[::-1])
            for char in templine:
                if char.isnumeric():
                    char2 = char
                    break
            num = int(char1 + char2)
            total += num
    return total

class TestMain(unittest.TestCase):

    def test_MainPart1(self):

        with mock.patch('__main__.yieldLineFromFile', return_value=['1']):
            rv = mainPart1('fake.data')
            self.assertEqual(11, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['12']):
            rv = mainPart1('fake.data')
            self.assertEqual(12, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['1','12']):
            rv = mainPart1('fake.data')
            self.assertEqual(23, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['1223']):
            rv = mainPart1('fake.data')
            self.assertEqual(13, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['a1']):
            rv = mainPart1('fake.data')
            self.assertEqual(11, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['2a']):
            rv = mainPart1('fake.data')
            self.assertEqual(22, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['1av4']):
            rv = mainPart1('fake.data')
            self.assertEqual(14, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['ca1av4z']):
            rv = mainPart1('fake.data')
            self.assertEqual(14, rv)

    def test_MainPart2(self):

        with mock.patch('__main__.yieldLineFromFile', return_value=['one']):
            rv = mainPart2('fake.data')
            self.assertEqual(11, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['onetwo']):
            rv = mainPart2('fake.data')
            self.assertEqual(12, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['one','onetwo']):
            rv = mainPart2('fake.data')
            self.assertEqual(23, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['onetwo2three']):
            rv = mainPart2('fake.data')
            self.assertEqual(13, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['afour']):
            rv = mainPart2('fake.data')
            self.assertEqual(44, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['fivea']):
            rv = mainPart2('fake.data')
            self.assertEqual(55, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['sixavseven']):
            rv = mainPart2('fake.data')
            self.assertEqual(67, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['caeightavninez']):
            rv = mainPart2('fake.data')
            self.assertEqual(89, rv)
        # overlap edge case where replace start from the beginning so two -> 2 at the end when it should be 1
        with mock.patch('__main__.yieldLineFromFile', return_value=['honemkmbfbnlhtbq19twonekbp']):
            rv = mainPart2('fake.data')
            self.assertEqual(11, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=
                        ['two1nine',
                         'eightwothree',
                         'abcone2threexyz',
                         'xtwone3four',
                         '4nineeightseven2',
                         'zoneight234',
                         '7pqrstsixteen']):
            rv = mainPart2('fake.data')
            self.assertEqual(281, rv)

if __name__ == '__main__':
    FILENAME = '1.data'
    RUNTEST = False

    if RUNTEST:
        unittest.main()
    else:
        print(mainPart2(FILENAME))