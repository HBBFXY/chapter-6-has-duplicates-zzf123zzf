def has_duplicates(lst):
    """判断列表中是否存在重复元素，存在则返回True，否则返回False"""
    # 利用集合元素唯一性的特性，比较原列表长度和集合长度
    return len(lst) != len(set(lst))


# 测试程序
if __name__ == "__main__":
    # 准备测试用例
    test_cases = [
        [1, 2, 3, 4, 5],       # 无重复元素
        [1, 2, 3, 2, 5],       # 有重复元素
        [],                     # 空列表
        [10],                   # 单元素列表
        ["a", "b", "a"],        # 字符串元素重复
        [1.5, 2.5, 1.5, 3.5],   # 浮点数元素重复
        [True, False, True]     # 布尔值元素重复
    ]
    
    # 执行测试并输出结果
    print("重复元素判定测试结果：")
    for i, case in enumerate(test_cases, 1):
        result = has_duplicates(case)
        print(f"测试用例 {i}: {case} → {'存在重复元素' if result else '无重复元素'}")
