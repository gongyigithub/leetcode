# coding=utf-8
"""
Oh, no! You have accidentally removed all spaces, punctuation, and capitalization in a lengthy document. A sentence like "I reset the computer. It still didn't boot!" became "iresetthecomputeritstilldidntboot''. You'll deal with the punctuation and capi­talization later; right now you need to re-insert the spaces. Most of the words are in a dictionary but a few are not. Given a dictionary (a list of strings) and the document (a string), design an algorithm to unconcatenate the document in a way that minimizes the number of unrecognized characters. Return the number of unrecognized characters.
有一个字符串，全部是小写，没有任何符号。给你一个字典，让你根据字典中的词在字符串里进行匹配，尽可能多的匹配上，使得最后剩下的单字符最少（字符串里大部分的单词都可以在字典中匹配到，小部分无法匹配）。返回最终没有匹配上的字符数
"""
"""
*********************
解题思路：DP，动态规划
"""


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if len(sentence) <= 0:
            return 0
        if len(dictionary) <= 0:
            return len(sentence)

        dp = [0] * (len(sentence) + 1)  # 最后一个0是哨兵
        for i in range(len(sentence)):
            dp[i] = dp[i - 1] + 1
            # 遍历所有单词，看能否和「以i为结尾的子串」一样
            for dic in dictionary:
                if (len(dic) <= i + 1) and sentence[i + 1 - len(dic):i + 1] == dic:
                    dp[i] = min(dp[i], dp[i - len(dic)])
        return dp[-2]
