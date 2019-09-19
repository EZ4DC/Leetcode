#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/9/19

# 罗马数字转整数
class Solution:
    def romanToInt(self, s):
        dic = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X': 10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(dic.get(s[max(i-1, 0):i+1], dic[n]) for i, n in enumerate(s))


