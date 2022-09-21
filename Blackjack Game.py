from Announcer import Announcer
from Dealer import Dealer
from Player import Player

playGame = input(("Would you like to play Blackjack? ('Y' or 'N'): "))

announcer = Announcer()

announcer.gameStart(playGame)

print()
while True:
    try:
        name = input("What is your name: ")
        balance = int(input("What is your initial balance: $"))
        break
    except:
        print("Invalid inputs. Try again.")


player = Player(name, balance)
dealer = Dealer()

print()
keepPlaying = "N"
while keepPlaying.lower() == "n":
    if player.getBalance() == 0:
        print("Can't play anymore. You ran out of money.")
        break

    announcer.intro(player.getName(), dealer.getName())
    player.setBet()

    print()
    announcer.shuffling()

    print()
    dealer.setCards()
    dealer.setCardsValue()

    announcer.initialDisplayCards(dealer.getPlayerCards(), dealer.getPlayerCardsValue(), dealer.getDealerCards(), dealer.getDealerCardsValue(), player.getName())

    print()
    answer = input("Would you like to hit or stand? ('Hit' or 'Stand'): ")

    breakOut = False
    #While player keeps hitting
    while announcer.hitOrStand(answer):
        print()
        dealer.dealExtraCard()
        if dealer.playerTotal > 21:
            breakOut = True
            break
        announcer.displayCards(dealer.getPlayerCards(), dealer.getPlayerCardsValue(), dealer.getDealerCards(), dealer.getDealerCardsValue(), player.getName())
        print()
        answer = input("Continue to hit or stand? ('Hit' or 'Stand'): ")

    #Runs after player stands or if they hit past 21
    if breakOut == False:
        announcer.finalDisplayCards(dealer.getPlayerCards(), dealer.getPlayerCardsValue(), dealer.getDealerCards(), dealer.getDealerCardsValue(), player.getName())
        print()
        if announcer.winLossChecker() == "tie":
            print("It ended in a tie!")
            player.tieBalance()
        elif announcer.winLossChecker() == "win":
            print("You win!")
            player.winBalance()
        elif announcer.winLossChecker() == "loss":
            print("The dealer wins!")
            player.lossBalance()
    elif breakOut:
        announcer.finalDisplayCards(dealer.getPlayerCards(), dealer.getPlayerCardsValue(), dealer.getDealerCards(), dealer.getDealerCardsValue(), player.getName())
        print()
        print("You lose!")
        player.lossBalance()

    print()
    keepPlaying = input("Would you like to stop playing: ('Y' or 'N'): ")
    print()
print("Thanks for playing!")