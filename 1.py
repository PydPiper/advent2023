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
'''

import unittest
from unittest import mock

# yield line from file
# loop fwd till you see a numeric
# loop backward till you see a numeric
# combine str and convert to int
# add int to running total

def yieldLineFromFile(filename:str) -> str:
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

def main(filename:str) -> int:
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

class TestMain(unittest.TestCase):

    def test_Main(self):

        with mock.patch('__main__.yieldLineFromFile', return_value=['1']):
            rv = main('fake.data')
            self.assertEqual(11, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['12']):
            rv = main('fake.data')
            self.assertEqual(12, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['1','12']):
            rv = main('fake.data')
            self.assertEqual(23, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['1223']):
            rv = main('fake.data')
            self.assertEqual(13, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['a1']):
            rv = main('fake.data')
            self.assertEqual(11, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['2a']):
            rv = main('fake.data')
            self.assertEqual(22, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['1av4']):
            rv = main('fake.data')
            self.assertEqual(14, rv)
        with mock.patch('__main__.yieldLineFromFile', return_value=['ca1av4z']):
            rv = main('fake.data')
            self.assertEqual(14, rv)

if __name__ == '__main__':
    FILENAME = '1.data'
    RUNTEST = False

    if RUNTEST:
        unittest.main()
    else:
        print(main(FILENAME))