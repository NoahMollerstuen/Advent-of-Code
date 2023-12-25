from collections import defaultdict

from util import *
from util import Grid as g
import itertools as it
import re

h = Helper(test_mode=False, test_input="""
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
""")

CARD_RANKS = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}


def score_hand(hand):
    score = 0
    m = 10e7
    for c in hand:
        score += m * c
        m /= 100
        # print(c, score)

    freqs = defaultdict(lambda: 0)
    for c in hand:
        freqs[c] += 1

    if 5 in freqs.values():
        score += 6e10
    elif 4 in freqs.values():
        score += 5e10
    elif 3 in freqs.values() and 2 in freqs.values():
        score += 4e10
    elif 3 in freqs.values():
        score += 3e10
    elif list(freqs.values()).count(2) == 2:
        score += 2e10
    elif 2 in freqs.values():
        score += 1e10

    print(hand, score)
    return score


inp = h.get_input_list()

input_hands = [([CARD_RANKS[c] for c in line.split(" ")[0]], int(line.split(" ")[1])) for line in inp]

scored_hands = []
for hand, bet in input_hands:
    score = score_hand(hand)
    scored_hands.append((hand, bet, score))

sorted_hands = sorted(scored_hands, key=lambda h: h[2], reverse=False)
print(sorted_hands)

winnings = 0
for i, hand in enumerate(sorted_hands):
    print((i + 1), hand[1])
    winnings += (i + 1) * hand[1]

h.submit(int(winnings))
