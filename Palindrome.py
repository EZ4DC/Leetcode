#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/9/19

# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
class Solution:
    def isPalindrome(self, x):
        #if x < 0:
        #    return False
        #else:
        #    num_list = list(str(x))
        #    new = num_list[::-1]
        #    return new == num_list
        num = 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        while x > num:
            num = num * 10 + x % 10
            x //= 10
        return x == num or x == num // 10

