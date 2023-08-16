import random

class Choice:
    def __init__(self, player1Choice, player2Choice):
        self.player1Choice = player1Choice
        self.player2Choice = player2Choice

    def getScore(self):
        if self.player1Choice == 'C' and self.player2Choice == 'C':
            return Score(3, 3)
        elif self.player1Choice == 'C' and self.player2Choice == 'D':
            return Score(0, 5)
        elif self.player1Choice == 'D' and self.player2Choice == 'C':
            return Score(5, 0)
        else:
            return Score(1, 1)

class Score:
    def __init__(self, player1Score, player2Score):
        self.player1Score = player1Score
        self.player2Score = player2Score

    def add(self, newScore):
        self.player1Score += newScore.player1Score
        self.player2Score += newScore.player2Score

    def __str__(self):
        return f"Player 1 Score: {self.player1Score}\nPlayer 2 Score: {self.player2Score}\n"

class Strategy1:
    def __init__(self, initialChoice):
        self.initialChoice = initialChoice

    def makeNextChoices(self, lastChoices, player):
        if len(lastChoices) == 0:
            if player == 1:
                return self.initialChoice.player1Choice
            else:
                return self.initialChoice.player2Choice
        if player == 1:
            return lastChoices[-1].player2Choice
        else:
            return lastChoices[-1].player1Choice

class Strategy2:
     def __init__(self, initialChoice):
        self.initialChoice = initialChoice

     def makeNextChoices(self, lastChoices, player):
        if len(lastChoices) < 2:
            if player == 1:
                return self.initialChoice.player1Choice
            else:
                return self.initialChoice.player2Choice
        
        if lastChoices[-1].player1Choice == "D" and lastChoices[-2].player1Choice == "D":
            player2NewChoice = "D"
        else:
            player2NewChoice = "C"

        if lastChoices[-1].player2Choice == "D" and lastChoices[-2].player2Choice == "D":
            player1NewChoice = "D"
        else:
            player1NewChoice = "C"

        if player == 1:
            return player1NewChoice
        else:
            return player2NewChoice

class Strategy3:
    def __init__(self, initialChoice):
        self.initialChoice = initialChoice
    def makeNextChoices(self, lastChoices, player):
        if len(lastChoices) < 2:
            if player == 1:
                return self.initialChoice.player1Choice
            else:
                return self.initialChoice.player2Choice
        player1ChoosedD = False
        player2ChoosedD = False
        for choice in lastChoices:
            if choice.player1Choice == "D":
                player1ChoosedD = True
            if choice.player2Choice == "D":
                player2ChoosedD = True
        if player1ChoosedD:
            player2NewChoice = "D"
        else:
            player2NewChoice = "C"

        if player2ChoosedD:
            player1NewChoice = "D"
        else:
            player1NewChoice = "C"
        if player == 1:
            return player1NewChoice
        else:
            return player2NewChoice

class Strategy4:
    def __init__(self, initialChoice):
        self.initialChoice = initialChoice
    def makeNextChoices(self, lastChoices, player):
        if len(lastChoices) == 0:
            if player == 1:
                return self.initialChoice.player1Choice
            else:
                return self.initialChoice.player2Choice     
        if lastChoices[-1].player2Choice == "D":
            if random.random() < 0.7:
                player1NewChoice = "D"
            else:
                player1NewChoice = "C"
        else:
            player1NewChoice = "C"

        if lastChoices[-1].player1Choice == "D":
            if random.random() < 0.7:
                player2NewChoice = "D"
            else:
                player2NewChoice = "C"
        else:
            player2NewChoice = "C"

        if player == 1:
            return player1NewChoice
        else:
            return player2NewChoice


class Game:
    def __init__(self, strategies, rounds = 100):
        self.choices = []
        self.strategies = strategies
        self.score = Score(0, 0)
        self.rounds = rounds

    def simulate(self):
        for i in range(len(self.strategies)):
            for j in range(i, len(self.strategies)):
                player1Strategy = self.strategies[i]
                player2Strategy = self.strategies[j]

                self.choices = []
                self.score = Score(0, 0)

                for _ in range(self.rounds):
                    nextPlayer1Choice = player1Strategy.makeNextChoices(self.choices, 1)
                    nextPlayer2Choice = player2Strategy.makeNextChoices(self.choices, 2)
                    nextChoice = Choice(nextPlayer1Choice, nextPlayer2Choice)
                    self.choices.append(nextChoice)
                    self.score.add(nextChoice.getScore())
                print("--------------------------")
                print(i + 1, j + 1)
                print(self.score)

                player1Choices = ""
                player2Choices = ""
                for k in self.choices:
                    player1Choices += k.player1Choice
                    player2Choices += k.player2Choice

                print(player1Choices)
                print(player2Choices)

game = Game([
    Strategy1(Choice("C", "D")),
    Strategy2(Choice("C", "D")),
    Strategy3(Choice("C", "D")),
    Strategy4(Choice("C", "D"))
])

game.simulate()