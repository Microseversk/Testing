import re
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        try:
            self.__checkInput__(s)
        except Exception as e:
            raise e

        for i in range(len(s)):
            res += self.__countPali__(s, i, i)
            res += self.__countPali__(s, i, i + 1)
        return res

    def __countPali__(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res

    def __checkInput__(self,s):
        if not(type(s) is str): raise TypeError(f"Incorrect input string type:${type(s)} expected ${type("")}")
        if not(re.fullmatch(r'^[a-z]+$',s)): raise AssertionError('Input string must contain only lowercases en letters')
        if not(len(s) > 0 and len(s) <= 1000): raise AssertionError('Input string length must be between 0 and 1001')

