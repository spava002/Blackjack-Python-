import random

class Dealer:

    cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    cardValues = {"Ace": [1, 11], "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
    name = ["Jude", "Oliver", "Matthew", "Jonathan", "Kyle", "Lily", "Alice"]
    dealerCards = []
    dealerCardsValue = []
    playerCards = []
    playerCardsValue = []

    def __init__(self):
        self.name = self.name[int(random.random() * len(self.name))]

    def getName(self):
        return self.name

    def getDealerCards(self):
        return self.dealerCards

    def getDealerCardsValue(self):
        return self.dealerCardsValue

    def getPlayerCards(self):
        return self.playerCards

    def getPlayerCardsValue(self):
        return self.playerCardsValue

    #Set cards based on their name
    def setCards(self):
        #Blank Slate
        self.dealerCards = []
        self.playerCards = []

        for i in range(2):
            self.dealerCards.append(self.cards[int(random.random() * len(self.cards))])
        for i in range(2):
            self.playerCards.append(self.cards[int(random.random() * len(self.cards))])

    #Set cards based on their value
    def setCardsValue(self):
        #Blank Slate
        self.dealerCardsValue = []
        self.playerCardsValue = []

        for i in range(2):
            if i == 1 and self.dealerCards[0] == "Ace" and self.dealerCards[1] == "Ace":
                self.dealerCardsValue.append(1)
            elif self.dealerCards[i] == "Ace":
                self.dealerCardsValue.append(11)
            else:
                self.dealerCardsValue.append(self.cardValues[self.dealerCards[i]])
        for i in range(2):
            if i == 1 and self.playerCards[0] == "Ace" and self.playerCards[1] == "Ace":
                self.playerCardsValue.append(1)
            elif self.playerCards[i] == "Ace":
                self.playerCardsValue.append(11)
            else:
                self.playerCardsValue.append(self.cardValues[self.playerCards[i]])

    def dealExtraCard(self):
        #Set Cards
        self.playerCards.append(self.cards[int(random.random() * len(self.cards))])

        #Get Player Total
        playerTotal = 0
        for i in self.playerCardsValue:
            playerTotal = playerTotal + i

        #Set Cards Value
        if self.playerCards[len(self.playerCards) - 1] == "Ace" and playerTotal <= 10:
            self.playerCardsValue.append(11)
        elif self.playerCards[len(self.playerCards) - 1] == "Ace" and playerTotal > 10:
            self.playerCardsValue.append(1)
        else:
            self.playerCardsValue.append(self.cardValues[self.playerCards[len(self.playerCards) - 1]])

        #Updated Player Total
        self.playerTotal = 0
        for i in self.playerCardsValue:
            self.playerTotal = self.playerTotal + i

        self.dealerTotal = 0
        for i in self.dealerCardsValue:
            self.dealerTotal = self.dealerTotal + i

        if self.dealerTotal < 16:
            #Set Cards
            self.dealerCards.append(self.cards[int(random.random() * len(self.cards))])
            #Set Cards Value
            if self.dealerCards[len(self.dealerCards) - 1] == "Ace" and self.dealerTotal <= 10:
                self.playerCardsValue.append(11)
                print("The dealer pulled an extra card.")
            elif self.dealerCards[len(self.dealerCards) - 1] == "Ace" and self.dealerTotal > 10:
                self.playerCardsValue.append(1)
                print("The dealer pulled an extra card.")
            else:
                self.dealerCardsValue.append(self.cardValues[self.dealerCards[len(self.dealerCards) - 1]])
                print("The dealer pulled an extra card.")