# my solution 

class Solution:
    def maxScore(self, s: str) -> int:
        s_len = len(s)
        fin_arr = []
        counter = 1
        while(counter < s_len):
            split = [counter]
            substrings = [s[start:end] for start, end in zip([0] + split, split + [None])]
            left_string = substrings[0]
            right_string= substrings[1]
            left_zero_count = left_string.count('0')
            right_one_count = right_string.count('1')
            fin_arr.append(left_zero_count+right_one_count)
            counter = counter + 1
        return max(fin_arr)


# O(N) -> beats 11% and 9% 

# best solution

class Solution:
    def maxScore(self, s: str) -> int:
        ones = 0
        zeros = 0
        best = -inf

        for i in range(len(s) - 1):
            if s[i] == "1":
                ones += 1
            else:
                zeros += 1
            
            best = max(best, zeros - ones)
            
        if s[-1] == "1":
            ones += 1
        
        return best + ones
    


# best runtime 

class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        for i in range(len(s)):
            right += 0 if s[i]=='0' else 1;
        for i in range(len(s)-1):
            left += 1 if s[i]=='0' else 0;
            right += 0 if s[i]=='0' else -1;
            ans = max(left+right,ans)
        return ans


        
        