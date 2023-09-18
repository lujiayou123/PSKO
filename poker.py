import random
# 定义扑克牌的四种花色和13种牌面
suits = ['h', 'd', 'c', 's']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# 生成一副标准扑克牌
deck = [rank + suit for rank in ranks for suit in suits]

def evaluate_hand(hand):
    # 在这里实现手牌评估逻辑，可以使用德州扑克规则进行评估
    # 你可以使用库或者自己编写规则来评估手牌的强度
    # 返回一个用于比较的分数，分数越高手牌越强
    pass

def compare_hands(player1_hand, player2_hand, community_cards="random"):
    # 计算玩家1和玩家2的手牌强度
    player1_score = evaluate_hand(player1_hand + community_cards)
    player2_score = evaluate_hand(player2_hand + community_cards)

    # 比较分数以确定胜者
    if player1_score > player2_score:
        return "玩家1胜利"
    elif player1_score < player2_score:
        return "玩家2胜利"
    else:
        return "平局"

def deal_hand(deck):
    print(len(deck))
    hands = random.sample(deck, 2)
    # 弹出被选中的元素
    for card in hands:
        deck.remove(card)
    print(len(deck))
    print(deck)
    return hands

# 输入两位玩家的手牌和公共牌
# player1_hand = ["As", "Ks"]  # 例如，Ace of Spades 和 King of Spades
# player2_hand = ["Qh", "Jh"]  # 例如，Queen of Hearts 和 Jack of Hearts
# community_cards = ["2s", "3s", "4s", "5h", "6d"]  # 公共牌

# result = compare_hands(player1_hand, player2_hand, community_cards)
# print(result)
if __name__ == '__main__':
    for i in range(26):
        hands = deal_hand(deck)
        print(hands)
    
