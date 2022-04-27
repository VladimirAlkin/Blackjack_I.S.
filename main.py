from strategies import *
from bj_game import *

""""Create players"""

d = Dealer("Dealer", 300, 2)
a = Player('Alice', 100, 1)
b = Player('Bob', 100, 3)
c = Player('Clod', 100, 1)
e = Player('Max', 100, 3)

""""Put players into list and list into the game"""

players = [a, b, c, e]
g = Game(d, players)

""""The game loop starts"""

while g.game_status != 'OVER':
    print("START OF A NEW ROUND\n\n")
    g.first_deal()
    for p in players:
        print(f"\n{p.name} cards")
        for c in p.hand:
            print(c)
        g.update_score(p)
        print(f'{p.name} SCORE: {p.score} \n STATUS: {p.status}')

    print('\nHIT OR STAND PART\n')

    for p in players:
        s = 'waiting for request'
        while s != 'stand':
            if p.strategy == 1:
                s = strategy1(p, g.dealer)
            if p.strategy == 3:
                s = strategy3(p, g.dealer)
            else:
                s = strategy2(p)
            if s == 'hit':
                g.hit(p)

    """"Player's cards and status after a round"""

    for p in players:
        print(f"\n{p.name} cards")
        for c in p.hand:
            print(c)
        print(f'\n{p.name} SCORE: {p.score} STATUS: {p.status}')

    g.end_of_round()
    print('\n\nROUND RESULTS:')

    for p in players:
        print(f'{p.name} SCORE: {p.score} BANK: {p.bank}')
        print()

    g.new_round()
