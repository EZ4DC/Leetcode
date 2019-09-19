#!/usr/bin/env python
# coding: UTF-8
# author: Dc Zheng time:2019/9/19

# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
class Solution:
    def reverse(self, x):
        #    rever = list(reversed(str(x)))
        #    if x > 0:
        #        while rever[0] == '0':
        #            rever.pop(0)
        #    if x < 0:
        #        while rever[0] == '0':
        #            rever.pop(0)
        #        rever.remove('-')
        #        rever.insert(0,'-')
        #    rever = ''.join(rever)
        #    if int(rever) < -2 ** 31 or int(rever) > 2 ** 31 -1:
        #        return 0
        #    else:
        #        return rever

        # 转为列表
        #    res = list(str(x))
        #    res.reverse()

        # 判断 第一项是否为0
        #    if res[0]==0:
        #        res.popleft()

        # 转为str
        #    ans = ''.join(res[:-1])

        # 判断最后一项
        #    if res[-1] == '-':
        #        ans = '-'+ans
        #    else:
        #        ans += res[-1]

        # 转为 int
        #    ans = int(ans)
        #    if  -2**31 <=ans<= 2**31-1:
        #        return ans
        #    else:
        #        return 0

        st = str(abs(x))
        st = ''.join(re.findall('(.*)0*', st))
        st = list(st)
        st.reverse()
        tag = 1 if x >= 0 else -1
        res = int(''.join(st[0:len(st)]))
        res = res if res >= -  2147483648 and res <= 2147483647 else 0
        return res * tag









