from strategies import *
from bj_game import *

d = Dealer("Dealer", 300, 3)
a = Player(input("Please - enter your player name: "), 100, 0)
b = Player('Bob', 100, 3)
c = Player('Clod', 100, 1)
e = Player('Max', 100, 2)

players = [a, b, c]
g = Game(d, players)

while g.game_status != 'OVER':

    print("START OF A NEW ROUND\n\n")
    g.first_deal()
    for p in players:
        print(f"\n{p.name} cards")
        for c in p.hand:
            print(c)
        g.update_score(p)
        print(f'{p.name} SCORE: {p.score} \nSTATUS: {p.status}')

    print('\nHIT OR STAND PART\n')

    for p in players:
        s = 'waiting for request'
        if p.name == a.name:
            while p.status != 'BUST':
                s = input('Type "hit" to receive a card, or type "stand" to not receive:  ')
                if s == 'stand':
                    break
                if s == 'hit':
                    g.hit(p)
                    print(f"\n{p.name} cards")
                    for c in p.hand:
                        print(c)
                    print(f'\n{p.name} SCORE: {p.score} STATUS: {p.status}')
                else:
                    print('Please enter "hit" or "stand"')
        else:
            while s != 'stand':
                if p.strategy == 1:
                    s = strategy1(p, g.dealer)
                if p.strategy == 3:
                    s = strategy3(p, g.dealer)
                else:
                    s = strategy2(p)
                if s == 'hit':
                    g.hit(p)

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

    print('Enter "OVER" to stop the game or just enter to continue: ')
    g.game_status = input()

    g.new_round()
