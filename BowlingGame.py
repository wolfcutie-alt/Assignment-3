class BowlingGame:
    """
    A class to represent a bowling game.
    """

    def __init__(self):
        """
        Initializes a new instance of the BowlingGame class.
        """
        self.rolls = []

    def roll(self, pins):
        """
        Records the number of pins knocked down in a single roll.

        Args:
            pins (int): The number of pins knocked down in the roll.
        """
        self.rolls.append(pins)

    def score(self):
        """
        Calculates the total score for the game.

        Returns:
            int: The total score for the game.
        """
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.StrikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """
        Determines if the roll at the specified index is a strike.

        Args:
            rollIndex (int): The index of the roll to check.

        Returns:
            bool: True if the roll is a strike, False otherwise.
        """
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """
        Determines if the roll and the next roll form a spare.

        Args:
            rollIndex (int): The index of the roll to check.

        Returns:
            bool: True if the two rolls form a spare, False otherwise.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def StrikeScore(self, rollIndex):
        """
        Calculates the score for a strike frame.

        Args:
            rollIndex (int): The index of the strike roll.

        Returns:
            int: The score for the strike frame, including bonuses.
        """
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        """
        Calculates the score for a spare frame.

        Args:
            rollIndex (int): The index of the first roll of the spare.

        Returns:
            int: The score for the spare frame, including the bonus.
        """
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """
        Calculates the score for a regular frame (not a strike or spare).

        Args:
            rollIndex (int): The index of the first roll in the frame.

        Returns:
            int: The score for the frame.
        """
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
