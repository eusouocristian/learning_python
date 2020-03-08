# unit test for the file 'moves.py' placed at the same folder
# to run, type 'python -m unittest <this_file_name.py>'
# documentation= https://docs.python.org/3/library/unittest.html
#---------------------------------------------------------------------------------------
# Main tests:
# setUp() - Method that is run before each test. Use this to set up state for the tests
# assertEqual(x, y) - Make sure x and y are equal
# assertNotEqual(x, y) - Make sure x and y are not equal
# assertGreater(x, y) - Make sure x is greater than y
# assertLess(x, y) - Make sure x is less than y
# assertIn(x, y) - Make sure x is a member of y (this is like the in keyword)
# assertIsInstance(x, y) - Make sure x is an instance of the y class
# assertGreaterEqual(x, y) - Make sure x is greater than or equal to y
# assertLessEqual(x, y) - Make sure x is less than or equal to y

import unittest
import moves

class MoveTests(unittest.TestCase):
    def setUp(self):
        self.rock = moves.Rock()
        self.paper = moves.Paper()
        self.scissors = moves.Scissors()
        

    def test_five_plus_five(self): # the name must iniciate with test_...
        assert 5 + 5 == 10
    
    def test_one_plus_one(self):
        assert not 1 + 1 == 3
    
    def test_equal(self):
        # rock1 = moves.Rock()
        # rock2 = moves.Rock()
        # self.assertEqual(rock1, rock2)
        self.assertEqual(self.rock, moves.Rock())

    def test_not_equal(self):
        # rock = moves.Rock()
        # paper = moves.Paper()
        # self.assertNotEqual(rock, paper)
        self.assertNotEqual(self.rock, self.paper)

    def test_rock_better_than_scissors(self):
        self.assertGreater(self.rock, self.scissors)

    def test_paper_worst_than_scissors(self):
        self.assertLess(self.paper, self.scissors)


# to run the code directly from debugger    
if __name__ == '__main__':
    unittest.main()

