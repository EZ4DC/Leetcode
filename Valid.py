#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/9/19

# 有效括号
class Solution:
    def isValid(self, s):
        stack = ['#']
        dic = {'{': '}', '[': ']', '(': ')', '#': '#'}
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1



