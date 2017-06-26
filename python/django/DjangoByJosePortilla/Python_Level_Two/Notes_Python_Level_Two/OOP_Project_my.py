#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle # I think the advantage of this is that it ONLY imports the "shuffle"
                            # instead of ALL of "random"
# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck():
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    cards = [] # make empyt deck list attribute for class

    def __init__(self):
        self.cards = self.makeDeck() # initialize func that makes a shuffled deck

    def makeDeck(self):
        # for x in SUITE:
        #     for y in RANKS:
        #         Deck.cards.append(x+y)
        # shuffle(Deck.cards)
        # MORE EFFICIENT WAY WITH LIST COMPREHENSIONS
        Deck.cards = [[s,r] for s in SUITE for r in RANKS]
        shuffle(Deck.cards) # must shuffle before return/print
        return Deck.cards

    def get_First_Half(self):
        return Deck.cards[:26]

    def get_Second_Half(self):
        return Deck.cards[26:]

class Hand():
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,stack):
        self.stack = stack

    def show_card(self):
        return self.stack[0]

    def remove_card(self):
        return self.stack.pop(0)

    def add_card(self,card):
        self.stack.append(card)

    def card_value(self,card_shown):
        ## return a number value for a face card
        if card_shown[1] == 'J':
            return 11
        elif card_shown[1] == 'Q':
            return 12
        elif card_shown[1] == 'K':
            return 13
        elif card_shown[1] == 'A':
            return 14
        else:
            return int(card_shown[1])


class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self,name,stack):
        self.name = name
        self.stack = stack

    def check_stack(self):
        ## make a function that checks how many cards are left in stack
        return len(self.stack)


#### IN GAME FUNCTIONS #####



def greeting(p1,p2):
    print("Hello {p1}, you'll be playing {p2}!".format(p1=p1,p2=p2))

def check_Card_Winner(p1_card,p2_card):
    ## return the losing card or False if it's a tie
    if p1.card_value(p1_card) > p2.card_value(p2_card):
        return p1_card
    elif p2.card_value(p2_card) > p1.card_value(p1_card):
        return p2_card
    elif p1.card_value(p1_card) == p2.card_value(p2_card):
        print("Going to war!")
        war()

def war():
    if p1.check_stack() > 4 and p2.check_stack() > 4:
        p1_war_stack = [p1_stack[1],p1_stack[2],p1_stack[3],p1_stack[4]]
        print(p1_war_stack)
        p2_war_stack = [p2_stack[1],p2_stack[2],p2_stack[3],p2_stack[4]]
        print(p2_war_stack)
        print(p1_war_stack[3], 'vs', p2_war_stack[3])
        winner = check_Card_Winner(p1_war_stack[3],p2_war_stack[3])
        print(winner)
        if winner == p1_war_stack[3]:
            for x in range(6):
                p1.add_card(p2.remove_card())
            print(p1.name, "won war!")
            print(p1.check_stack())
            print(p2.check_stack())
        elif winner == p2_war_stack[3]:
            for x in range(6):
                p2.add_card(p1.remove_card())
            print(p2.name, "won war!")
            print(p2.check_stack())
            print(p1.check_stack())
        else:
            print("No winner for this war. Removing cards.")
            for x in range(6):
                p1.remove_card()
                p2.remove_card()

def check_Game_Winner():
    if p1.check_stack() > p2.check_stack():
        print("Game OVER!",p1.name," won!!!")
        return False
    else:
        print("Game OVER!",p2.name," won!!!")
        return False

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
new_Deck = Deck()
p1_stack = new_Deck.get_First_Half()
p2_stack = new_Deck.get_Second_Half()
# for x in p1_stack:
#     for y in p2_stack:
#         if x == y:
#             print("another equal card")
p1 = Player(input("Player 1, what is your name? "),p1_stack)
p2 = Player(input("Player 2, what is your name? "),p2_stack)
greeting(p1.name,p2.name)




### TEST RUN ###
# print(p1.show_card(), 'vs',p2.show_card())
# if check_Card_Winner(p1.show_card(),p2.show_card()) != False:
#     if check_Card_Winner(p1.show_card(),p2.show_card()) == p1.show_card():
#         p1.add_card(p2.remove_card())
#         print(p1.name," won, and gets the card.")
#     elif check_Card_Winner(p1.show_card(),p2.show_card()) == p2.show_card():
#         p2.add_card(p1.remove_card())
#         print(p2.name," won, and gets the card.")
play = True
while play == True:
    if p1.check_stack() > 3 and p2.check_stack() > 3:
        card_move_to_end = []
        print(p1.show_card(), 'vs',p2.show_card())
        if check_Card_Winner(p1.show_card(),p2.show_card()) != False:
            if check_Card_Winner(p1.show_card(),p2.show_card()) == p1.show_card():
                p1.add_card(p2.remove_card())
                card_move_to_end = p1.remove_card()
                p1.add_card(card_move_to_end) # puts first card at the end
                print(p1.name," won, and gets the card.")
                print(p1.name,": ",p1.check_stack())
                print(p2.name,": ",p2.check_stack())
            elif check_Card_Winner(p1.show_card(),p2.show_card()) == p2.show_card():
                p2.add_card(p1.remove_card())
                card_move_to_end = p2.remove_card()
                p2.add_card(card_move_to_end) # puts first card at the end
                print(p2.name," won, and gets the card.")
                print(p1.name,": ",p1.check_stack())
                print(p2.name,": ",p2.check_stack())
    else:
        print("Checking for winner now.")
        play = check_Game_Winner()
    answer = input("Type 'y', if want to continue, or 'n' if you want to quit.")
    if answer == 'y':
        play = True
    elif answer == 'n':
        play = False
    else:
        print("Bad input, quitting game.")
        play = False

























###### THIS TEST CODE WORKS: Check for reference if needed.#############

# print("Welcome to War, let's begin...")
# new_Deck = Deck()
# p1_stack = new_Deck.splitDeck()[0]
# p2_stack = new_Deck.splitDeck()[1]
# p1 = Player("Logan",p1_stack)
# p2 = Player("Tiffany",p2_stack)
# # p1_hand = Hand(p1_stack)
# # p2_hand = Hand(p2_stack)
# print("P1: show",p1.show_card())
# p1_removed_card = p1.remove_card()
# print("P1: card that was removed: ",p1_removed_card)
# print("P2: show last:",p2_stack[-1])
# p2.add_card(p1_removed_card)
# print("hand being added...")
# print("P2: show last:",p2_stack[-1])
# print("P1: show",p1.show_card())
# print("P1: removed",p1.remove_card())
# print("P1: show",p1.show_card())
# print("P1 stack amount: ",p1.check_stack())
# print("P2 stack amount: ",p2.check_stack())
