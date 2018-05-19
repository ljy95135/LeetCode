# str.index (sub, start=None, end=None)
# ValueError: substring not found or lowest index
#

# str.find (sub, start=None, end=None) -1 or lowest index
# for highest index: rindex rfind

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if every time not found: O(n^2)
        if s == "":
            return 0
        curr_result = max_result = 1
        start = 0
        end = 1
        for i, v in enumerate(s):
            if i == 0:
                continue
            h_index = s.rfind(v, start, end)
            if h_index == -1:
                # -1: add this one
                curr_result += 1
                max_result = max(curr_result, max_result)
            else:
                start = h_index + 1
                curr_result = end - h_index
            end += 1
        return max_result
