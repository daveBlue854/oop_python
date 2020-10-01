from enum import IntFlag


class BetOdds(IntFlag):
    STRAIGHT = 35
    SPLIT = 17
    STREET = 11
    CORNER = 8
    FIVE_BET = 6
    LINE = 5
    DOZEN = 2
    COLUMN = 2
    EVEN_MONEY = 1
