import random


def strategy1(player, dealer):
    player_value = player.score
    dealer_value = dealer.score

    if player_value < dealer_value:
        return 'hit'

    if player.hand_status == 'soft':
        if player_value < 17:
            return 'hit'
        elif player_value > 18:
            return 'stand'
        else:
            if random.choice([0, 1]):
                return 'hit'
            else:
                return 'stand'
    else:
        if player_value < 11:
            return 'hit'
        elif player_value > 17:
            return 'stand'
        else:
            return 'hit'


def strategy2(dealer):
    dealer_value = dealer.score
    if dealer_value < 17:
        return 'hit'
    else:
        return 'stand'


def strategy3(player, dealer):
    pvalue = player.score
    dvalue = dealer.score

    if 17 <= dvalue <= 21:  # Dealer pat hand
        if pvalue < dvalue:
            return 'hit'
    elif 7 <= dvalue <= 11:
        if pvalue <= dvalue or 12 <= pvalue <= 15:
            return 'hit'
    elif dvalue < 7:
        if pvalue < 12:
            return 'hit'
        elif player.hand_status == 'soft' and pvalue < 16:
            return 'hit'

    if player.hand_status == 'hard' and 12 <= dvalue <= 16:  # Dealer "stiff" hand
        if pvalue < dvalue:
            return 'hit'
        elif player.hand_status == 'soft' and pvalue <= 16:
            return 'hit'

    if player.hand_status == 'hard' and 12 <= dvalue <= 16:
        if pvalue <= 12:
            return 'hit'
        elif player.hand_status == 'soft' and pvalue <= 18:
            return 'hit'

    return 'stand'
