def has_five_consecutive(nums):
    # 确保列表中有且仅有七个元素
    if len(nums) != 7:
        return False

    # 对列表进行排序
    sorted_nums = sorted(nums)

    # 遍历排序后的列表，查找连续的五个整数
    for i in range(len(sorted_nums) - 4):
        if sorted_nums[i + 4] - sorted_nums[i] == 4:
            return True

    return False


# 测试代码
nums = [3, 1, 4, 5, 6, 9, 7]
result = has_five_consecutive(nums)
if result:
    print("列表中存在五个连续的整数")
else:
    print("列表中不存在五个连续的整数")
