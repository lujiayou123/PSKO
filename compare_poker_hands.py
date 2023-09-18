#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File            :compare_poker_hands.py
@Introduction    :比较手牌大小
@CreateTime      :2023/09/18 21:42:09
@Author          :Sulyvahn
@Version         :1.0
'''

# 定义扑克牌的权值，这里使用字典来映射
card_value_dict = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}
'''
是否存在顺子
@Parameters    :
  nums- 手牌+牌面，一共七张牌
@Returns       : 是否存在顺子
@Raises        : KeyError - raises an exception
'''


def has_five_consecutive(nums):

    # 对列表进行排序
    sorted_nums = sorted(nums)

    # 遍历排序后的列表，查找连续的五个整数
    length = len(sorted_nums)
    for i in range(length - 4):
        if sorted_nums[length - 1 - i] - sorted_nums[length - 5 - i] == 4:
            five_consecutive = sorted_nums[length - 5 - i:length - i]
            return True, five_consecutive
    # 将A替换成1
    new_nums = [x if x != 14 else 1 for x in sorted_nums]
    sorted_new_nums = sorted(new_nums)
    length = len(sorted_new_nums)
    for i in range(length - 4):
        if sorted_new_nums[length - 1 - i] - sorted_new_nums[length - 5 -
                                                             i] == 4:
            five_consecutive = sorted_new_nums[length - 5 - i:length - i]
            return True, five_consecutive
    return False, []


'''
判断是否是同花顺
@Parameters    :
  hand- 手牌
  board- board
@Returns       : True, [5cards]
@Raises        : KeyError - raises an exception
'''


def is_straight_flush(hand, board):
    """
    Checks if a player has a straight flush

    checks if it is a straight by comparing if there is a consecutive group of 5 numbers. Then checks if they are all the
    same suit.

    Args:
        player : player instance

    Returns:
        True if the hand is a straight flush and false if not
    """
    board = hand + board
    card_suits = [card[1] for card in board]
    unique_suits = []
    same_suit = False
    for suit in card_suits:
        if suit not in unique_suits:
            unique_suits.append(suit)

    final_suit = [suit for suit in unique_suits if card_suits.count(suit) >= 5]

    if len(final_suit) == 1:
        same_suit = True

    if same_suit:
        check_royal_flush = [
            card for card in board if card[1] == final_suit[0]
        ]
        check_nums = [
            card_value_dict[card[0]] for card in check_royal_flush
            if card[1] == final_suit[0]
        ]
        check_nums.sort()
        has_five, five_consecutive = has_five_consecutive(check_nums)
        print(five_consecutive)
        if has_five:
            suit = final_suit[0]
            made_hand = [
                card for card in board
                if card[0] in five_consecutive and card[1] == suit
            ]
            return True, made_hand
        else:
            return False, []
    else:
        return False, []


'''
判断是否是四条
@Parameters    :
  hand- 手牌
  board- board
@Returns       : True, [5cards]
@Raises        : KeyError - raises an exception
'''


def is_quards(hand, board):
    """
    Checks if a hand contains four of a kind by checking if there is a number that repeats itself 4 times in a hand.

    Args:
        player: player instance

    Returns:
        True if the hand is a four of a kind, false if not
    """
    board = hand + board
    card_nums = [card[0] for card in board]
    four_nums = [num for num in card_nums if card_nums.count(num) == 4]

    if len(four_nums) == 4:
        made_hand_four = [card for card in board if card[0] == four_nums[0]]
        left_nums = [num for num in card_nums if num not in four_nums]
        kicker = [card for card in board if card[0] == max(left_nums)]
        made_hand = made_hand_four + kicker
        return True, made_hand[0:5]
    else:
        return False, []


'''
判断是否是fullhouse
@Parameters    :
  hand- 手牌
  board- board
@Returns       : True, [5cards]
@Raises        : KeyError - raises an exception
'''


def is_full_house(hand, board):
    """
    Checks if a hand is a full house

    checks if there is a group of 3 same cards, and a group of 2 same cards. If there is both, it is a full house.

    Args:
        player: player instance

    Returns:
        True if it is a full house, false if not
    """
    board = hand + board
    card_nums = [card[0] for card in board]
    three_group = [num for num in card_nums if card_nums.count(num) == 3]
    two_group = [num for num in card_nums if card_nums.count(num) == 2]
    # 3+2
    if len(three_group) == 3 and len(two_group) >= 2:
        made_hand_three = [card for card in board if card[0] == three_group[0]]
        made_hand_two = [card for card in board if card[0] == two_group[0]]
        made_hand = made_hand_three + made_hand_two
        return True, made_hand[0:5]
    # 3+3
    elif len(three_group) == 6 and len(two_group) == 0:
        two_three_kind = list(set(three_group))
        card1, card2 = two_three_kind[0], two_three_kind[1]
        if card_value_dict[card1] > card_value_dict[card2]:
            big_card, small_card = card1, card2
        else:
            big_card, small_card = card2, card1
        made_hand_three = [card for card in board if card[0] == big_card]
        made_hand_two = [card for card in board if card[0] == small_card]
        made_hand = made_hand_three + made_hand_two
        return True, made_hand[0:5]
    else:
        return False, []


'''
判断是否是同花
@Parameters    :
  hand- 手牌
  board- board
@Returns       : True, [5cards]
@Raises        : KeyError - raises an exception
'''


def is_flush(hand, board):
    """
    Checks if a hand is a Flush

    checks if there is a group of 5 or more cards with the same suit

    Args:
        player: player instance

    Returns:
        True if it is a flush, false if not
    """
    board = hand + board
    card_suits = [card[1] for card in board]

    unique_suits = []
    same_suit = False
    for suit in card_suits:
        if suit not in unique_suits:
            unique_suits.append(suit)

    final_suit = [suit for suit in unique_suits if card_suits.count(suit) >= 5]

    if len(final_suit) == 1:
        same_suit = True

    if same_suit:
        filtered_cards = [card for card in hand if card[0] in final_suit]

        flush_nums = list(map(lambda card: int(card[1:]), flush_cards))
        flush_nums.sort()
        if 1 in flush_nums:
            player.comparison_card = 1
        else:
            player.comparison_card = flush_nums[-1]
        return True


if __name__ == '__main__':
    hand1 = ['4c', 'Tc']
    # board = ['2c', '2h', '2s', 'Th', '3d']
    board = ['2c', 'Jc', 'Kc', 'Qc', 'Ac']
    print(is_full_house(hand1, board))
    print(is_quards(hand1, board))
    print(is_straight_flush(hand1, board))
