#import libraries
import unittest
import Blackjack_sim

#creating an object from unittest testcase
class monte(unittest.TestCase):
 
#capture test results for play() function
    def test_play(self):
        result = Blackjack_sim.play()
        expected= 0
        self.assertEqual(expected,result)
#check for expected output
if __name__ == "__main__":
    unittest.main()
