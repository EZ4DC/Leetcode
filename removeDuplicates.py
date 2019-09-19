#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/9/19

# 原地删除重复出现的元素
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k

