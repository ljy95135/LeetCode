# using a dict {char: last_index}
# do not need to del key if their index < start
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars_map = {}
        curr_res = max_res = 0
        start = 0
        for i, v in enumerate(s):
            if v not in chars_map or chars_map[v] < start:
                curr_res += 1
                max_res = max(max_res, curr_res)
            else:
                start = chars_map[v] + 1
                curr_res = i - start + 1
            chars_map[v] = i

        return max_res
