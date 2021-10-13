import random


class Deck:
    def __init__(self):
        self.deck = {
            'Clubs of Two': 2,
            'Clubs of Three': 3,
            'Clubs of Four': 4,
            'Clubs of Five': 5,
            'Clubs of Six': 6,
            'Clubs of Seven': 7,
            'Clubs of Eight': 8,
            'Clubs of Nine': 9,
            'Clubs of Ten': 10,
            'Clubs of Jack': 10,
            'Clubs of Queen': 10,
            'Clubs of King': 10,
            'Clubs of Ace': 11,
            'Diamonds of Two': 2,
            'Diamonds of Three': 3,
            'Diamonds of Four': 4,
            'Diamonds of Five': 5,
            'Diamonds of Six': 6,
            'Diamonds of Seven': 7,
            'Diamonds of Eight': 8,
            'Diamonds of Nine': 9,
            'Diamonds of Ten': 10,
            'Diamonds of Jack': 10,
            'Diamonds of Queen': 10,
            'Diamonds of King': 10,
            'Diamonds of Ace': 11,
            'Hearts of Two': 2,
            'Hearts of Three': 3,
            'Hearts of Four': 4,
            'Hearts of Five': 5,
            'Hearts of Six': 6,
            'Hearts of Seven': 7,
            'Hearts of Eight': 8,
            'Hearts of Nine': 9,
            'Hearts of Ten': 10,
            'Hearts of Jack': 10,
            'Hearts of Queen': 10,
            'Hearts of King': 10,
            'Hearts of Ace': 11,
            'Spades of Two': 2,
            'Spades of Three': 3,
            'Spades of Four': 4,
            'Spades of Five': 5,
            'Spades of Six': 6,
            'Spades of Seven': 7,
            'Spades of Eight': 8,
            'Spades of Nine': 9,
            'Spades of Ten': 10,
            'Spades of Jack': 10,
            'Spades of Queen': 10,
            'Spades of King': 10,
            'Spades of Ace': 11
        }

    def shuffle(self):
        shuffling = list(self.deck.items())
        random.shuffle(shuffling)
        self.deck = dict(shuffling)

    def deal(self):
        card_from_deck = next(iter(self.deck.items()))
        del self.deck[next(iter(self.deck))]
        return card_from_deck


class Card:
    def __init__(self, card):
        self.card = card
        self.name = card[0]
        self.value = card[1]


class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 100

    def bet(self, chips):
        if self.chips > chips:
            return chips
        else:
            return None

    def hit(self):
        pass

    def stand(self):
        pass


class Dealer:
    def __init__(self):
        self.card = ""


class Pot:
    def __init__(self):
        self.chips = 0

    def add_to_pot(self, chips):
        self.chips = self.chips + chips


while True:

    # Greeting message
    print("Welcome to Toby's Blackjack")

    # Creates deck + shuffles
    deck_One = Deck()
    deck_One.shuffle()

    # Create Player Objects
    number_of_players = int(input("How many Players?: "))
    players = []
    pots = []
    for i in range(number_of_players):
        players.append(Player(input(f"Whats the name of player{i + 1}?: ")))
        pots.append(Pot())
    print(type(players[0].name))

    # Main game logic
    for i in range(len(players)):
        bet = int((input(f"How much do {players[i].name} want to bet?: ")))
        pots[i].add_to_pot(players[i].bet(bet))
        print(f"{players[i].name} sendt {bet} to the Pot and the pot is now on {pots[i].chips}")

    # Dealer deals the cards to players and himself
    cards = []
    for i in range(len(players)+1):
        cards.append(Card())




deck = Deck()
deck.shuffle()

print(f"Welcome {player_1.name}")
print(player_1.chips)
print("how much you want to bet")

player_1.chips = 35
print(player_1.chips)
pot_1.add_to_pot(player_1.bet(40))

print(pot_1.chips)

# card = Card(deck.deal())

# print(deck.deck)
# print(card.name)
