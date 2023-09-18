import random

# 定义扑克牌的四种花色和13种牌面
suits = ['H', 'D', 'C', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# 生成一副标准扑克牌
deck = [rank + suit for rank in ranks for suit in suits]

# 模拟一次德州扑克的比赛
def simulate_game(player1_hand, player2_range):
    # 随机生成公共牌，这里生成3张公共牌
    board = random.sample(deck, 3)
    
    # 计算每个玩家的最终手牌
    player1_final_hand = player1_hand + board
    player2_final_hand = random.sample(player2_range, 2) + board
    
    # 使用手牌比较库来确定胜者
    # 在实际应用中，你可能需要实现一个手牌比较函数
    # 这里简单地将玩家1和玩家2的牌打印出来以示比较
    print("Player 1:", player1_final_hand)
    print("Player 2:", player2_final_hand)
    
    # 返回比赛结果，1表示玩家1获胜，-1表示玩家2获胜，0表示平局
    return 1 if player1_final_hand > player2_final_hand else (-1 if player2_final_hand > player1_final_hand else 0)

# 计算equity的函数
def calculate_equity(player1_hand, player2_range, num_simulations):
    player1_wins = 0
    player2_wins = 0
    ties = 0
    
    for _ in range(num_simulations):
        result = simulate_game(player1_hand, player2_range)
        if result == 1:
            player1_wins += 1
        elif result == -1:
            player2_wins += 1
        else:
            ties += 1
    
    player1_equity = player1_wins / num_simulations
    player2_equity = player2_wins / num_simulations
    tie_equity = ties / num_simulations
    
    return player1_equity, player2_equity, tie_equity

# 示例输入
player1_hand = ['As', 'Ad']  # 玩家1的手牌
player2_range = random.sample(deck, 10)  # 玩家2的对手范围，这里随机选择了10张牌
num_simulations = 10000  # 模拟次数

# 计算equity
player1_equity, player2_equity, tie_equity = calculate_equity(player1_hand, player2_range, num_simulations)

# 打印结果
print("Player 1 Equity:", player1_equity)
print("Player 2 Equity:", player2_equity)
print("Tie Equity:", tie_equity)
