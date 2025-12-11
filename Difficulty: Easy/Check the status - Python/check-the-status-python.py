class Solution:
    def checkStatus(self, a, b, flag):
        # code here
        if (a < 0 and b < 0 and flag):
            return True
            
        elif (((a > 0 and b < 0) or (a < 0 and b > 0)) and not flag):
            return True
        
        return False