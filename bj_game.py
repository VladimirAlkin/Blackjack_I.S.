import random


def create_deck():
    suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(Card(rank, suit))
    return deck


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        if self.rank.isnumeric():
            return int(self.rank)
        elif self.rank == 'A':
            return 'A'
        else:
            return 10

    def __str__(self):
        return f"{self.suit} : {self.rank}"


# I don't see the way to put object Hand into this system 'cause all Hand's functions are implemented in Player.
# All player does is - holding. Holding his name, bank, cards, cards / hand status and score
#
class Player:
    def __init__(self, name, bank, strategy):
        self.name = name
        self.bank = bank
        self.strategy = strategy
        self.hand = []
        self.hand_status = 'hard'
        self.status = 'PLAYING'
        self.score = 0

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self, cards):
        self.__hand = cards


class Dealer(Player):

    def deal_cards(self, deck, players):
        random.shuffle(deck)
        for player in players:
            player.hand.append(deck.pop())
            player.hand.append(deck.pop())


class Game:
    deck = create_deck()
    game_status = 'ON'

    def __init__(self, dealer, players: list):
        self.dealer = dealer
        self.players = players
        players.append(dealer)
        if len(players) > 6 or len(players) == 0:
            print('The game must include from 2 to 6 players')
            return

    def first_deal(self):
        self.dealer.deal_cards(self.deck, self.players)

    def update_score(self, player):
        player.score = 0
        ace_flag_counter = 0
        for card in player.hand:
            card_value = card.get_value()
            if card_value == 'A':
                ace_flag_counter += 1
                player.score = player.score + 11
                player.hand_status = 'soft'  # if A counted as 11 - the hand is soft
            else:
                player.score = player.score + card_value
        for i in range(0,
                       ace_flag_counter):  # if player has A and player got more than 21 this loop will recount every A to 1 instead of 11
            if player.score > 21:
                player.score = player.score - 10
                player.hand_status = 'hard'

        self.upd_player_status(player)

    def hit(self, player):
        if player.status == 'BUST':
            return 'Player lost'
        player.hand.append(self.deck.pop())
        self.update_score(player)
        self.upd_player_status(player)

    def upd_player_status(self, player):
        if player.score == 21:
            player.status = 'WIN'
        elif player.score > 21:
            player.status = 'BUST'

    def new_round(self):
        self.deck = create_deck()
        for player in self.players:
            player.hand = []
            player.score = 0
            player.status = 'PLAYING'

    # Dealer don't lose bank if he got lower score than a player.
    def end_of_round(self):
        player_21_flag = False
        players_max_score = 0
        for player in self.players:
            if player.status == 'WIN' and self.dealer.status != 'WIN':
                player.bank += 1
                player_21_flag = True
            elif player.score > self.dealer.score and player.status != 'BUST':
                player.bank += 1
            elif player.status != 'BUST' and self.dealer.status == 'BUST':
                player.bank += 1
            elif player.status == 'BUST':
                player.bank -= 1
            elif player.score < self.dealer.score and self.dealer.status != 'BUST':
                player.bank -= 1
            if player.score > players_max_score and player.status != 'BUST':
                players_max_score = player.score

        if self.dealer.status == 'WIN' and player_21_flag == False:
            self.dealer.bank += 1
        elif self.dealer.score > players_max_score and self.dealer.status == 'PLAYING':
            self.dealer.bank += 1

        for player in self.players:
            if player.bank == 0:
                self.players.remove(player)
                if player == self.dealer:
                    self.game_status = 'OVER'
                if len(self.players) < 2:
                    self.game_status = 'OVER'

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, players):
        self.__players = players


