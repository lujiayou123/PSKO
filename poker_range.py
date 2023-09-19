from itertools import combinations
import copy
from unittest import main

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['s', 'h', 'd', 'c']
suit_flags = ['s', 'o']
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


def assure_range_correct(range_str):
    assert len(range_str) >= 2 and len(range_str) <= 4, "范围输入错误"
    assert range_str[0] in ranks and range_str[1] in ranks, "范围输入错误"
    assert card_value_dict[range_str[0]] >= card_value_dict[
        range_str[1]], "范围输入错误"
    if len(range_str) == 2:
        assert range_str[0] == range_str[1], "范围输入错误"
    if len(range_str) == 3:
        if range_str[0] == range_str[1]:
            assert range_str[2] == "+", "范围输入错误"
        else:
            assert range_str[2] in suit_flags, "范围输入错误"
    if len(range_str) == 4:
        assert range_str[0] != range_str[1] and range_str[
            2] in suit_flags and range_str[3] == "+", "范围输入错误"


def singleRange2Hand(range_str):
    # 确保输入范围正确
    assure_range_correct(range_str)
    # 对子
    if len(range_str) == 2:
        card = range_str[0]
        pool = [card + suit for suit in suits]
        hand_combinations = list(combinations(pool, 2))
        return hand_combinations
    # AKs / 22+
    if len(range_str) == 3:
        card1 = range_str[0]
        card2 = range_str[1]
        # 22+
        if card1 == card2:
            higher_cards = []
            for element in card_value_dict:
                if card_value_dict[element] >= card_value_dict[card1]:
                    higher_cards.append(element)
            hand_combinations = []
            for card in higher_cards:
                pool = [card + suit for suit in suits]
                combos = list(combinations(pool, 2))
                hand_combinations = hand_combinations + combos
            return hand_combinations
        # AKs/AKo
        else:
            # suited
            suit_flag = range_str[2]
            if suit_flag == "s":
                hand_combinations = []
                for suit in suits:
                    pool = [card1 + suit, card2 + suit]
                    combos = list(combinations(pool, 2))
                    hand_combinations = hand_combinations + combos
                return hand_combinations
            # off suit
            elif suit_flag == "o":
                pool1 = [card1 + suit for suit in suits]
                pool2 = [card2 + suit for suit in suits]
                pool = pool1 + pool2
                combos = list(combinations(pool, 2))
                hand_combinations = copy.deepcopy(combos)
                # remove pairs and suited combos
                for combo in combos:
                    # remove pairs
                    if combo[0][0] == combo[1][0]:
                        hand_combinations.remove(combo)
                    # remove suited
                    if combo[0][1] == combo[1][1]:
                        hand_combinations.remove(combo)
                return hand_combinations
            else:
                print("Error, Neither s Nor o")
                return []
    # ATs+ / ATo+
    if len(range_str) == 4:
        high_card = range_str[0]
        kicker_card = range_str[1]
        higher_cards = []
        for element in card_value_dict:
            if card_value_dict[element] >= card_value_dict[
                    kicker_card] and card_value_dict[
                        element] < card_value_dict[high_card]:
                higher_cards.append(element)
        print(higher_cards)
        # suited
        suit_flag = range_str[2]
        if suit_flag == "s":
            hand_combinations = []
            for kicker in higher_cards:
                for suit in suits:
                    pool = [high_card + suit, kicker + suit]
                    combos = list(combinations(pool, 2))
                    hand_combinations = hand_combinations + combos
            return hand_combinations
        # off suit
        elif suit_flag == "o":
            hand_combinations = []
            for kicker in higher_cards:
                pool1 = [high_card + suit for suit in suits]
                pool2 = [kicker + suit for suit in suits]
                pool = pool1 + pool2
                all_combos = list(combinations(pool, 2))
                kicker_combos = copy.deepcopy(all_combos)
                # remove pairs and suited combos
                for combo in all_combos:
                    # remove pairs
                    if combo[0][0] == combo[1][0]:
                        kicker_combos.remove(combo)
                    # remove suited
                    if combo[0][1] == combo[1][1]:
                        kicker_combos.remove(combo)
                hand_combinations += kicker_combos
            return hand_combinations
        else:
            print("Error, Neither s Nor o")
            return []


if __name__ == '__main__':
    # 示例用法
    range_str = "AQo+"
    hand_combinations = singleRange2Hand(range_str)
    print("具体的手牌组合:", len(hand_combinations), hand_combinations)
