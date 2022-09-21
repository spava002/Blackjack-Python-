from Dealer import Dealer
from Player import Player

class Announcer:

    name = ""

    def __init__(self):
        pass

    def gameStart(self, playGame):
        if playGame.lower() == "y":
            print("Great! Let us begin.")
        elif playGame.lower() == "n":
            print("'Till next time!")
            exit()
        else:
            playGame = input(("I didn't understand. Please input 'Y' or 'N': "))
            Announcer.gameStart(self, playGame)

    def intro(self, playerName, dealerName):
        print(f"Hello {playerName} your dealer for today will be {dealerName}.")

    def shuffling(self):
        print("Dealing cards...")

    def initialDisplayCards(self, playerCards, playerCardsValue, dealerCards, dealerCardsValue, playerName):
        print("The dealer has dealt the following cards:")
        if dealerCardsValue[0] > dealerCardsValue[1]:
            print("Dealer: '" + dealerCards[0] + f"' and '?'. (Total of: " + str(dealerCardsValue[0]) + ").")
        elif dealerCardsValue[1] > dealerCardsValue[1]:
            print("Dealer: '" + dealerCards[1] + f"' and '?'. (Total of: " + str(dealerCardsValue[1]) + ").")
        else:
            print("Dealer: '" + dealerCards[0] + f"' and ?. (Total: " + str(dealerCardsValue[0]) + ").")

        playerTotal = playerCardsValue[0] + playerCardsValue[1]
        print(f"{playerName}: '" + playerCards[0] + "' and '" + playerCards[1] + f"'. (Total of: {playerTotal}).")

    #Prints new cards, but still with "?" to hide dealer's card.
    def displayCards(self, playerCards, playerCardsValue, dealerCards, dealerCardsValue, playerName):
        #Dealer's Cards
        if dealerCardsValue[0] > dealerCardsValue[1]:
            dealerTotal = dealerCardsValue[0]
        else:
            dealerTotal = dealerCardsValue[1]
        print("Dealer: '" + dealerCards[0] + "' ", end = "")
        for i in range(len(dealerCards) - 1):
            print("'?' ", end = "")
        print(f"(Total of: {dealerTotal})")

        #Player's Cards
        playerTotal = 0
        for i in playerCardsValue:
            playerTotal = playerTotal + i
        print(f"{playerName}: ", end = "")
        for i in playerCards:
            print("'" + i + "' ", end = "")
        print(f"(Total of: {playerTotal})")

    #Prints new cards, but now shows dealer's hidden card(s)
    def finalDisplayCards(self, playerCards, playerCardsValue, dealerCards, dealerCardsValue, playerName):
        #Dealer's Cards
        self.dealerTotal = 0
        for i in dealerCardsValue:
            self.dealerTotal = self.dealerTotal + i

        print("Dealer: '", end = "")

        for i in dealerCards:
            print(i + "' ", end = "")

        print(f"(Total of: {self.dealerTotal})")

        #Player's Cards
        self.playerTotal = 0
        for i in playerCardsValue:
            self.playerTotal = self.playerTotal + i

        print(f"{playerName}: '", end = "")

        for i in playerCards:
            print(i + "' ", end = "")

        print(f"(Total of: {self.playerTotal})")

    def hitOrStand(self, answer):
        while True:
            if answer.lower() == "hit" or answer.lower() == "h":
                return True
            elif answer.lower() == "stand" or answer.lower() == "s":
                return False
            else:
                answer = input("I don't understand your input. Enter 'Hit' or 'Stand': ")

    def winLossChecker(self):
        #Check who wins in the end
        if self.dealerTotal > 21 and self.playerTotal > 21:
            return "tie"
        elif self.dealerTotal > 21:
            return "win"
        elif self.playerTotal > 21:
            return "loss"
        elif self.dealerTotal > self.playerTotal:
            return "loss"
        elif self.playerTotal > self.dealerTotal:
            return "win"
        elif self.dealerTotal == self.playerTotal:
            return "tie"