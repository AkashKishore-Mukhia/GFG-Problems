#User function Template for python3
class Solution:
	def removeDuplicates(self, s):
	    # code here
	    
	    upper_char_cnt = [0 for _ in range(26)]
	    lower_char_cnt = [0 for _ in range(26)]
	    
	    result = ''
	    
	    for c in s:
	        c_asscii = ord(c)
	        if c_asscii < 97:
	            index = c_asscii - ord('A')
	            if upper_char_cnt[index] < 1:
	                result += c
	           
	            upper_char_cnt[index] += 1
	                
	       
	        else:
	            index = c_asscii - ord('a')
	            if lower_char_cnt[index] < 1:
	                result += c
	   
	            lower_char_cnt[index] += 1
	    
	    return result
	            
	    