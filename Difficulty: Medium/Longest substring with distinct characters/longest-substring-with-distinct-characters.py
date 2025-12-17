class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        alpha = [0 for _ in range(26)]
        
        i, j = 0, 0
        n = len(s)
        result = 0
        while j < n:
            charidx = ord(s[j]) - 97
            alpha[charidx] += 1
            if alpha[charidx] > 1:
                while alpha[charidx] > 1:
                    alpha[ord(s[i]) - 97] -= 1
                    i += 1
            else:
                result = max(result, j-i+1)

            j += 1
            
        return result