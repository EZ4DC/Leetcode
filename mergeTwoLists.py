#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/9/19

# 合并两个有序链表
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2

