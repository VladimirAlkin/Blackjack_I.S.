|| BLACKJACK I.S. ||

blackjack_IS is Intellectual Simulation of a Blackjack game.

The game can contain 2-6 players.
The game ends when there's one player left or a dealer got busted (lost).
Simulated players use 1 of 3 strategies wich are implemented from strategies.py.
Whole game rules, players scores, cards and checks are at bj_game.py.

Run main.py for simulation.
At this simulation 4 players and the dealer.
Players use strategies 1 or 3. The dealer use his own strategy - 2.
Every player got bank of 100. Dealer got 300.

Run main_solo_playing.py to play your self.
Enter name of your player and every HIT OR STAND part - you'll be asked to enter a command.
Enter 'hit' to take a card. Enter 'stand' to stay with cards you have.
At the end of each round you can enter 'OVER' to end the game or just press Enter to continue.


THE GAME LOOP:

At the start of each round object dealer use deal_cards().

After that every player makes a choise - hit or stand. At this stage player's score and status get updated.

After hit or stand part - the game checks everyone's score, win conditions and distributes the bank with end_of_round().
At the end of the round the game execute new_round() and starts the loop from the beginning till
the end of game conditions will be achieved.



FUNCTIONS MENTIONED:

deal_cards() - deal two random cards for each player from the list.

hit() - player gets 1 random card and execute update_status() and update_score().

update_score() - counts player's score within the rules of the game. Also changes hand_status to 'soft' or 'hard' by
checking if Ace in the hand counted as 11 or 1.

update_status() - if players score is more than 21 - changes players status to 'BUST'. If it equals to 21 - to 'WIN'.

end_of_round() - checks every player and the dealer for their win conditions, distributes the bank of every player,
checks if a player have to be removed from the players list [if players bank = 0].

new_round() - resets the deck, removes all cards from every players, resets players scores to 0, resetes players
status to 'PLAYING'.
