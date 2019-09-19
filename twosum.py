#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/9/19

# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution:
    def twoSum(self, nums, target):
        #
        # length = len(nums)
        # for i, element in enumerate(nums):
        #    j = i + 1
        #    while j < length:
        #        if (element + nums[j]) == target:
        #            return [i, j]
        #            j += 1

        # 模拟哈希
        hashmap = {}
        for i, element in enumerate(nums):
            hashmap[element] = i

        for j, num in enumerate(nums):
            n = hashmap.get(target - num)
            if n is not None and n != j:
                return [j, n]




