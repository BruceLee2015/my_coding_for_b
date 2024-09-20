def longest_subarray(nums, target):
    left = 0  # 滑动窗口的左边界
    current_sum = 0  # 当前窗口内元素的和
    max_length = 0  # 最长子数组的长度

    for right in range(len(nums)):  # 右边界从左到右遍历数组
        current_sum += nums[right]  # 将当前元素加入到窗口中

        # 当当前窗口的和大于目标值时，移动左边界直到窗口的和小于或等于目标值
        while current_sum > target:
            current_sum -= nums[left]
            left += 1

        # 如果当前窗口的和等于目标值，更新最长子数组的长度
        if current_sum == target:
            max_length = max(max_length, right - left + 1)

    return max_length

# 示例
nums = [1, 15, 7, 9, 2, 5, 10]
target = 9
print(longest_subarray(nums, target))  # 输出应该是 3
print("testtesttest")