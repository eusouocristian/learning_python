# unit test for the file 'moves.py' placed at the same folder
# to run, type 'python -m unittest <this_file_name.py>'

import unittest
import moves

class MoveTests(unittest.TestCase):
    def test_five_plus_five(self):
        assert 5 + 5 == 10
    
    def test_one_plus_one(self):
        assert not 1 + 1 == 3

# to run the code directly from debugger    
if __name__ == '__main__':
    unittest.main()
