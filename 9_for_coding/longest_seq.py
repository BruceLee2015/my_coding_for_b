# 128. 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为O(n) 的算法解决此问题。

def longestConsecutive(nums):
    num_set = set(nums)  # 去重作用
    res = 0
    for num in num_set:
        if (num - 1) not in num_set:
            seq = 1
            while (num + 1) in num_set:
                seq += 1
                num += 1
        res = max(seq, res)
    return res


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))

# 标准答案
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         res = 0     # 记录最长连续序列的长度
#         num_set = set(nums)     # 记录nums中的所有数值
#         for num in num_set:
#             # 如果当前的数是一个连续序列的起点，统计这个连续序列的长度
#             if (num - 1) not in num_set:
#                 seq_len = 1     # 连续序列的长度，初始为1
#                 while (num + 1) in num_set:
#                     seq_len += 1
#                     num += 1    # 不断查找连续序列，直到num的下一个数不存在于数组中
#                 res = max(res, seq_len)     # 更新最长连续序列长度
#         return res
#
# 作者：画图小匠
# 链接：https://leetcode.cn/problems/longest-consecutive-sequence/solutions/2362995/javapython3cha-xi-biao-ding-wei-mei-ge-l-xk4c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
