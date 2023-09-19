from treys import Card, Deck, Evaluator
from itertools import combinations
import time


def determine_winner(player1_hand, player2_hand, board):
    evaluator = Evaluator()
    p1_score = evaluator.evaluate(board, player1_hand)
    p2_score = evaluator.evaluate(board, player2_hand)
    p1_class = evaluator.get_rank_class(p1_score)
    p2_class = evaluator.get_rank_class(p2_score)
    # print("Player 1 hand rank = %d (%s)\n" %
    #       (p1_score, evaluator.class_to_string(p1_class)))
    # print("Player 2 hand rank = %d (%s)\n" %
    #       (p2_score, evaluator.class_to_string(p2_class)))
    if p1_score < p2_score:
        return 1
    elif p1_score > p2_score:
        return -1
    else:
        return 0


'''
两个手牌跑一遍，分胜负
@Parameters    :
  hand1- [card1, card2]
  hand2- [card1, card2]
@Returns       : [equity1, equity2]
@Raises        : KeyError - raises an exception
'''


def hand_vs_hand_RunItOnce(hand1, hand2, board=None):
    evaluator = Evaluator()
    # 洗牌
    deck = Deck()
    # 发牌
    player1_hand = deck.deal_specific_hand(hand1)
    player2_hand = deck.deal_specific_hand(hand2)
    print(Card.ints_to_pretty_str(player1_hand))
    print(Card.ints_to_pretty_str(player2_hand))
    if board is None:
        board = deck.draw(5)
    print(Card.ints_to_pretty_str(board))
    p1_score = evaluator.evaluate(board, player1_hand)
    p2_score = evaluator.evaluate(board, player2_hand)
    p1_class = evaluator.get_rank_class(p1_score)
    p2_class = evaluator.get_rank_class(p2_score)
    print("Player 1 hand rank = %d (%s)\n" %
          (p1_score, evaluator.class_to_string(p1_class)))
    print("Player 2 hand rank = %d (%s)\n" %
          (p2_score, evaluator.class_to_string(p2_class)))
    if p1_score < p2_score:
        return 1
    elif p1_score > p2_score:
        return -1
    else:
        return 0


def hand_vs_hand_equity(hand1, hand2, borad=None):
    # 列举所有牌面
    deck = Deck()
    player1_hand = deck.deal_specific_hand(hand1)
    player2_hand = deck.deal_specific_hand(hand2)
    # 枚举所有牌面组合
    if borad is None:
        board_combos = list(combinations(deck.cards, 5))
    number_of_total_hands = len(board_combos)
    number_of_hands_beaten = 0
    number_of_hands_chopped = 0
    number_of_hands_lost = 0
    for board_combo in board_combos:
        board_combo = list(board_combo)
        result = determine_winner(player1_hand, player2_hand, board_combo)
        if result == 1:
            number_of_hands_beaten += 1
        elif result == -1:
            number_of_hands_lost += 1
        else:
            number_of_hands_chopped += 1
        print(number_of_hands_beaten, number_of_hands_lost,
              number_of_hands_chopped)
    equity1 = (number_of_hands_beaten +
               number_of_hands_chopped) / number_of_total_hands
    equity2 = (number_of_hands_lost +
               number_of_hands_chopped) / number_of_total_hands
    return equity1, equity2


'''
计算具体的手牌面对整个范围的Equity
@Parameters    :
  hand_list- 手牌, [Ad,Kd]
  ranges_str- "AQo+,AJs+,88+,KQs"
@Returns       : This is a description of what is returned
@Raises        : KeyError - raises an exception
'''


def hand_vs_range(hand_list, ranges_str):
    pass


if __name__ == '__main__':
    start_time = time.time()
    hand1 = ["Ad", "Kd"]
    hand2 = ["Qd", "Jd"]
    # equity1, equity2 = hand_vs_hand_RunItOnce(hand1, hand2)
    # print(f"hand1:{hand1} {equity1}, hand2:{hand2} {equity2}")
    # for i in range(100):
    #     print(i)
    #     result = hand_vs_hand_RunItOnce(hand1, hand2)
    #     if result == 0:
    #         print(result)
    #         break
    e1, e2 = hand_vs_hand_equity(hand1, hand2)
    print(e1, e2)
    end_time = time.time()
    print(f"cost_time:{end_time-start_time}")
