import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score()==0
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score()==20
    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.score()==300
    def testOneSpare(self):
        self.rollMany(5,21)
        assert self.game.score()==150
    def testTwoSpare(self):
        self.game.rolls(2)
        self.game.rolls(8)
        self.game.rolls(3)
        self.game.rolls(7)
        self.game.rolls(4)
        self.rollMany(0, 15)
        assert self.game.score() == 31
    def testTwoStrike(self):
        self.game.rolls(10)
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(2)
        self.rollMany(0, 14)
        assert self.game.score() == 46
    def rollMany(self, pins,rolls):
        for i in range(rolls):
            self.game.rolls(pins)
            
    if __name__ == '__main__':
        unittest.main()