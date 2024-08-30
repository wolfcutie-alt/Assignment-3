import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)  
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    def testOneStrike(self):
        self.game.roll(10)  
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    def testPerfectGame(self):
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    def testAllFives(self):
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150)

    def testTwoSpare(self):
        self.game.roll(2)
        self.game.roll(8)  
        self.game.roll(3)
        self.game.roll(7)  
        self.game.roll(4)
        self.rollMany(0, 15)
        self.assertEqual(self.game.score(), 31)

    def testTwoStrike(self):
        self.game.roll(10)  
        self.game.roll(10)  
        self.game.roll(4)
        self.game.roll(2)
        self.rollMany(0, 14)
        self.assertEqual(self.game.score(), 46)

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()