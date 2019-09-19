#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/9/19

# 最长公共前缀
class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        for tmp in zip(*strs):
            tmp_new = set(tmp)
            if len(tmp_new) == 1:
                res += tmp[0]
            else:
                break
        return res


