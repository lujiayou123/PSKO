'''
计算起始赏金在不同阶段的筹码比值
@Parameters    :
  remaining_percentage- left_players/total_players
@Returns       : This is a description of what is returned
@Raises        : KeyError - raises an exception
'''


def calculate_bounty_worth_ratio(remaining_percentage):
    a = 0.1411764705882353
    b = -0.2917647058823529
    c = 0.40058823529411763
    return remaining_percentage * remaining_percentage * a + b * remaining_percentage + c

'''
计算所call入需要的equity
@Parameters    :
  curPot- 当前底池大小(not call yet)
  toCall- 需要call入的码量
  bountyMagnification- 赢下底池时，能拿到的赏金的倍数(即赏金总数除以起始赏金)
  startingChips- 起始筹码量
  left_players- 还剩下多少名玩家
  total_players- 总共报名参赛的玩家
@Returns       : This is a description of what is returned
@Raises        : KeyError - raises an exception
'''


def calculate_equity_to_call(curPot, toCall, bountyMagnification, startingChips, left_players, total_players):
    remaining_percentage = left_players/total_players
    bounty_worth_ratio = calculate_bounty_worth_ratio(remaining_percentage)
    correspondingChips_per_staringBounty = startingChips * bounty_worth_ratio
    bounty_chips = correspondingChips_per_staringBounty * bountyMagnification
    pot = curPot + toCall + bounty_chips
    equity = toCall / pot
    return equity
'''
计算所bounty的价值
@Parameters    :
  bountyMagnification- 赏金的倍数(即赏金总数除以起始赏金)
  startingChips- 起始筹码量
  left_players- 还剩下多少名玩家
  total_players- 总共报名参赛的玩家
  remaining_percentage- 剩下多少名玩家的比例
@Returns       : This is a description of what is returned
@Raises        : KeyError - raises an exception
'''


def calculate_bounty_worth(bountyMagnification, startingChips, left_players, total_players):
    remaining_percentage = left_players/total_players
    bounty_worth_ratio = calculate_bounty_worth_ratio(remaining_percentage)
    bounty_chips = startingChips * bounty_worth_ratio * bountyMagnification
    return bounty_chips

if __name__ == '__main__':
    equity = calculate_equity_to_call(curPot=7000, toCall=5992, bountyMagnification=1, startingChips=10000, left_players=484, total_players=771)
    print(equity)
    print(calculate_bounty_worth_ratio(0.9))
